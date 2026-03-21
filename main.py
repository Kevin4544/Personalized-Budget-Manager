import datetime

from financer import Account
import bud

# Object created from Account class from financer.py
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

monthly_income = float(input("To begin, enter your monthly income: $"))
#monthly income will remain the same, income is the one that will change
income = monthly_income
#This variable leads to the budget method we'll use, it starts off as none
chosen_bud = None

#Main loop starts here
while True:
    print("What would you like to do?")
    print("1. Add an expense")
    print("2. View an expense")
    print("3. Check balance")
    print("4. Start a budgeting method")
    print("5. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1": #Add an expense

        #This is where the data is collected from the user
        exp_type = my_acc.choose_expense()  
        if exp_type == -1:
            continue
        if exp_type == None:
            exp_type = my_acc.choose_expense()

        cost = float(input("How much did you spend? "))

        # Store as a dictionary and add to our list along with current date 
        my_acc.add_expense(exp_type, cost)

        #need budget checking method here, might use it to replace the next few lines
        income -= cost 
        print(f"Remaining income: ${income:.2f}\n")
        if cost > income:
            print("Warning: You have exceeded your monthly income.\n")

        if chosen_bud != None:
            bud.analyze(chosen_bud, income, my_acc.expense_list())

    elif choice == "2": #View an expense
        print("\nExpense List") 
        see_history()      
        
    elif choice == "3": #Check total balance
        
        print(f"Current income: {income:.2f}")
        print("Which balance type would you like to see?")
        my_acc.see_balance()

    elif choice == "4": #Choose budgeting method using info from bud.py
        
        chosen_bud = bud.choose_method()
        if chosen_bud == -1:
            continue
        bud.analyze(chosen_bud, monthly_income, my_acc.expense_list())

    elif choice == "5": #Exit
        print ("Goodbye!")
        break #This breaks the while loop and ends it

    else:
        print("Invalid choice, please try again.")