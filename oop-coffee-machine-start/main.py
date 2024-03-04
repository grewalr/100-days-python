from menu import Menu, MenuItem
from coffee_maker import coffee_maker
from money_machine import money_machine

end = False
coffee_maker = coffee_maker()
money_machine = money_machine()
menu = Menu()
REPORT = "report"
OFF = "off"

while not end:
    items = menu.get_items()
    command = input(f"What would you like? ({items}): ").lower()

    if command == OFF:
        end = True
    elif command == REPORT:
        coffee_maker.report()
        money_machine.report()
    else:
        beverage = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(beverage) and money_machine.make_payment(beverage.cost):
            coffee_maker.make_coffee(beverage)
