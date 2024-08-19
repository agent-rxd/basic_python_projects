print("Welcome to leap year checker ")
year=int(input("Enter the year you wish to check : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year," is a Leap Year !")
        else:
            print(year," is not a leap year !")
    else:
       print(year," is  a Leap Year !")
else:
    print(year," is not a leap year !")
    