def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    drinks = {
        "espresso": {"water": 50, "coffee": 18, "price": 1.5},
        "latte": {"water": 200, "milk": 150, "coffee": 24, "price": 2.5},
        "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "price": 3.0}
    }

    def print_report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")

    def check_resources(drink):
        for ingredient, amount in drinks[drink].items():
            if ingredient != "price" and resources[ingredient] < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins():
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.1
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total

    def make_coffee(drink):
        for ingredient, amount in drinks[drink].items():
            if ingredient != "price":
                resources[ingredient] -= amount
        print(f"Here is your {drink}. Enjoy!")

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice in drinks:
            if check_resources(choice):
                payment = process_coins()
                if payment >= drinks[choice]["price"]:
                    change = round(payment - drinks[choice]["price"], 2)
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    resources["money"] += drinks[choice]["price"]
                    make_coffee(choice)
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print("Invalid input. Please try again.")

coffee_machine()