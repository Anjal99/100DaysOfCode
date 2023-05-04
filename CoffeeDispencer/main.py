from coffee import MENU, resources

money = 0
maintenance = True

def checkResource(drinkIngredients):
    '''
        Returns a boolean depending on the resources left in the machine
    '''
    for item in drinkIngredients:
        if drinkIngredients[item] >= resources[item]:
            print(f"Sorry there's not enough {item}")
            return False
    return True

def takePayment():
    '''
        Returns the total sum of money that the user's added
    '''
    print('Please insert coins')
    q = int(input('how many quarters?:'))
    d = int(input('how many dimes?:'))
    n = int(input('how many nickles?:'))
    p = int(input('how many pennies?:'))

    # Calculate the amount of money entered by the user
    total = (q * 0.25) + (d * 0.10) + (n * 0.5) + (p * 0.01)
    return total

def verifyTransaction(userPayment, purchasePrice):
    '''
        Checks to see if the user entered sufficient coins for the drink ordered
    '''
    if userPayment >= purchasePrice:
        global money
        money += purchasePrice
        change = round(userPayment - purchasePrice, 2)
        print(f"Here's your change ${change}")
        return True
    else:
        print("Sorry insufficient funds were entered. Refunding the money!")
        return False

def makeDrink(drink, drinkIngredients):
    '''
        Takes into account the resource used and prints the beverage result
    '''
    for item in drinkIngredients:
        resources[item] -= drinkIngredients[item]
    
    print(f"Here's your {drink}!")

def main():
    global maintenance
    while maintenance:
        # Prompt the user for a drink selection
        selectDrink = input("What would you like to have? (Espresso - $1.5/Latte - $2.5/Cappuccino - $3.0): ").lower()

        # Turn the machine off
        if selectDrink == 'off':
            maintenance = False
        elif selectDrink == 'report':
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
            print(f"Money : {money}")
        else:
            drink = MENU[selectDrink]
            if checkResource(drink['ingredients']):
                payment = takePayment()
                if verifyTransaction(payment, drink["cost"]):
                    makeDrink(selectDrink, drink["ingredients"])


main()