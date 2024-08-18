print("Welcome to Rolercoaster Checker !")
height=float(input("Enter your height in centimeters : "))
if height >= 120:
    print("You can enjoy this ride !")
    age=int(input("Enter your age : "))
    if age <= 18:
        print("Please pay $10")
    else:
        print("Please pay $15")
else:
    print("Sorry ! Your are not tall enough to enjoy this ride .")