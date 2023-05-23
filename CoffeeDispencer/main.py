from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Things to do

'''
-> Ask the user to make a choice for coffee drink
-> Turn 'off' and get the report
-> Check if the resources are sufficient 
-> Process coins
-> Check if the transaction was successful
-> Make the coffee
'''

items = Menu() # Initialize the Menu Object
coffee = CoffeeMaker() # Initialize the CoffeeMaker Object
money = MoneyMachine()
nextCustomer = True

while nextCustomer:
    # Prompt the user for a drink
    drinkOptions = input(f'What would you like? {items.get_items()}: ').lower()

    # Get the report if the option is report or exit program if option is off
    if drinkOptions == 'report':
        print(coffee.report(), money.report())
    elif drinkOptions == 'off':
        nextCustomer = False
    else:
        chosenDrink = items.find_drink(drinkOptions)
        resources = coffee.is_resource_sufficient(chosenDrink)
        if resources:
            # Process coins
            # Check if transaction is successful
            checkPayment = money.make_payment(chosenDrink.cost)

            if checkPayment:
                # Make the coffee
                coffee.make_coffee(chosenDrink)