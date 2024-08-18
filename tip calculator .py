print("---------------------------------")
print("| WELCOME TO RXD TIP CALCULATOR |")
print("---------------------------------")
a=float(input("What was the total bill ? : $"))
b=float(input("How much tip wold you like to give ? [10 , 12 or 15] : "))
a=((b/100)*a)+a
c=float(input("How many people to split the bill ? : "))
d=round(a/c,2)
print("Each person should pay : ",d," !")