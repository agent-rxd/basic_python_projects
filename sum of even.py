num=int(input("Enter a number upto which you wish to add : "))
choice=int(input("""1. Add odd number\n2. Add even numbers\nEnter your choice : """))
tot=0
if choice==2:
    ch="even"
    for i in range(0,num+1,2):
        tot=tot+i
    print("The sum of all even numbers till ",num," is ",tot)

else:
    for i in range(1,num+1,2):
        tot=tot+i
    print("The sum of all even numbers till ",num," is ",tot)




