import random
print("Welcome to RXD Automated Password Generator!")
secur=input("How secure do you want your password to be : [normal , medium , high ] : ")
sec=secur.lower()
if sec=="normal":
    num_ltr=random.randint(11,16)
    num_sym=round((20/100)*num_ltr)
    num_num=round((20/100)*num_ltr)
elif sec=="medium":
    num_ltr=random.randint(16,26)
    num_sym=round((25/100)*num_ltr)
    num_num=round((25/100)*num_ltr)
else:
    num_ltr=random.randint(26,41)
    num_sym=round((30/100)*num_ltr)
    num_num=round((30/100)*num_ltr)
ltrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
syms = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_list = []
for i in range(1,num_ltr+1):
    pass_list+=random.choice(ltrs)
for i in range(1,num_num+1):
    pass_list+=random.choice(nums)
for i in range(1,num_sym+1):
    pass_list+=random.choice(syms)
random.shuffle(pass_list)
passwrd =""
for i in range(1,num_ltr):
    passwrd+=pass_list[i]
print(f"Your password is : {passwrd}" )

