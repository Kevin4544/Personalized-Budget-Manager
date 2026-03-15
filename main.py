import pandas as pd
import datetime

from financer import Account
import bud

# Object created from Account class
my_acc = Account()

# Method for viewing expenses
# Couldn't make it work through the financer, will stay here for now
def see_history():
    exp_history = my_acc.expense_list()

    if not exp_history:
        print("\nYou have no expenses on record.\n")
        return
    
    for record in exp_history:
        print(f"{record['Spending Type']}: ${record['Cost']:.2f}")
        

    

print("\nHello! Welcome to your Personal Finance Tracker.")
print("This program will help you budget and track your expenses.\n")

income = float(input("To begin, enter your monthly income: $"))

#Main loop starts here
while True:
    print("What would you like to do?")
    print("1. Add an expense")
    print("2. View an expense")
    print("3. Check balance")
    print("4. Start a new budgeting method")
    print("5. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1": #Add an expense

        #This is where the data is collected from the user
        exp_type = my_acc.choose_expense()  
        while exp_type == None:
            exp_type = my_acc.choose_expense()

        cost = float(input("How much did you spend? "))

        # Store as a dictionary and add to our list along with current date 
        my_acc.add_expense(exp_type, cost)

        #need budget checking method here, might use it to replace the next few lines
        income -= cost 
        print(f"Remaining income: ${income:.2f}\n")
        if cost > income:
            print("Warning: You have exceeded your monthly income.\n")

    elif choice == "2": #View an expense
        print("\nExpense List") 
        see_history()      
        
    elif choice == "3": #Check total balance
        
        print(f"Current income: {income:.2f}")
        print("Which balance type would you like to see?")
        my_acc.see_balance()

    elif choice == "4": #Choose budgeting method using info from bud.py
        method = bud.choose_method()


    elif choice == "5": #Exit
        print ("Goodbye!")
        break #This breaks the while loop and ends it

    elif choice == "6": #View full dataframe of expenses (just for testing purposes)

        #I need to get the finances dictionary here but with the data already recorded in it
        df = pd.DataFrame(my_acc.finances)
        print(df.head())
else:
        print("Invalid choice, please try again.")