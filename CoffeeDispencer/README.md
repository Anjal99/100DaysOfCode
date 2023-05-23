## Object Oriented Coffee Machine Concept

Under the OOP Folder, the coffee machine program is broken down into multiple class files which demostrate a working Object-Class concept for a coffee dispencing program. 

### Program Requirements
1) Prompt the user to make a selection from the drink menu
2) The coffee machine has 2 more inputs it can take:
    'off' to turn the machine of for maintenance
    'report' to chekc the status of the machine's resources and revenue generated
3) Check for sufficient resources and take in the payment method. 
4) Validate the transaction
5) Make and dispense user's beverage

### Code Walkthrough

### Main.py
Here is where the program 

### coffee_maker.py
Within this class, we attempt to print the report, check for resources with the machine as well as make the coffee for the user.

### menu.py
This class models the menu for our coffee machine. Here, we walk through the menu item to search for the coffee choice that the user has made.

### money_machine.py
Here, we validate the user's payment method, process the transaction and append the profits to our report. Based on the validation, a trigger is created to dispence coffee or return/decline the payment option.
