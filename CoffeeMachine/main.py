from data import MENU, resources

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"


def generate_report(current_resources):
    return f"""
Water: {current_resources["water"]}ml
Milk: {current_resources["milk"]}ml
Coffee: {current_resources["coffee"]}g
Money: ${round(current_resources["money"], 2)}
"""

def is_enough_resources(current_resources, command):
    ingredients = MENU[command]["ingredients"]

    if current_resources["water"] < ingredients["water"]:
        print("Sorry there is not enough water")
        return False
    elif current_resources["coffee"] < ingredients["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    elif command == LATTE or command == CAPPUCCINO:
        if current_resources["milk"] < ingredients["milk"]:
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    else:
        return True


def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = float((quarters * QUARTER) + (dimes * DIME) + (nickles * NICKEL) + (pennies * PENNY))

    return total


def check_transaction_successful(current_resources, command, paid):
    beverage = MENU[command]
    ingredients = beverage["ingredients"]
    cost = beverage["cost"]

    # Check to see if we need to give change
    if paid > cost:
        change = round(paid - cost, 2)
        print(f"Here is ${change} in change")
        print(f"Here is your {command} ♨️Enjoy!")

        current_resources["money"] = round((current_resources["money"] + cost), 2)
        current_resources["water"] -= ingredients["water"]
        current_resources["coffee"] -= ingredients["coffee"]

        if command == LATTE or command == CAPPUCCINO:
            current_resources["milk"] -= ingredients["milk"]
    else:
        print(f"Sorry that's not enough money. Money refunded")

    return current_resources


def coffee_machine():
    resources["money"] = 0
    current_resources = resources
    end = False
    print(generate_report(current_resources))

    while not end:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if command == "off":
            end = True
        elif command == "report":
            print(generate_report(current_resources))
        elif command == ESPRESSO or command == LATTE or command == CAPPUCCINO:
            if is_enough_resources(current_resources, command):
                total = process_coins()
                current_resources = check_transaction_successful(current_resources, command, total)

                print(current_resources)
        else:
            end = True


coffee_machine()
