import pandas as pd
import datetime

def choose_exp():
    print("\n1. Groceries \n2. Rent \n3. Utilities \n4. Entertainment \n5. Other \n6. Cancel\n")
    in_exp = input("Enter the type of expense: ")
    exp = in_exp.strip()

    match exp:
        case "1":
            return "Groceries"
        case "2":
            return "Rent"
        case "3":
            return "Utilities"
        case "4":
            return "Entertainment"
        case "5": #other
            return input("\nPlease specify the type of expense: ")
        case "6":
            print("\nCancelled.\n")
            return None
        case _:
            print("\nInvalid choice, please try again.\n")
            return None

#Initialize an empty list to store a list of the user's finances.
finances = []

print("\nHello! Welcome to your Personal Finance Tracker.")
print("This program will help you budget and track your expenses.\n")

income = float(input("Please enter your monthly income: "))
# This income value might need to get moved to a separate file, for now its just a variable here.

#Main loop starts here
while True:
    print("What would you like to do?")
    print("1. Add an expense")
    print("2. View an expense")
    print("3. Check total balance")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        #This is where the data is collected from the user
        exp = choose_exp()
        
        cost = float(input("How much did you spend? "))

        # Store as a dictionary and add to our list along with current date 
        entry = {"item": exp, "cost": cost, "date": datetime.datetime.now().strftime("%m/%d/%Y")}
        finances.append(entry)
        print(f"Stored: {exp} for ${cost:.2f}")

        income -= cost 
        print(f"Remaining Balance: ${income:.2f}\n")

        if cost > income:
            print("Warning: You have exceeded your monthly income.\n")

    elif choice == "2":
        print("\nExpense List")
        #A 'for' loop to iterate through our list
        for record in finances:
            print(f"* {record['item']}: ${record['cost']:.2f}\n")

    elif choice == "3":
        
        print("Which expenses would you like to see?")
        print("1. All expenses \n2. By category \n3. By date \n4. Cancel\n")
        
        in_view = input("Enter your choice: ")
        view = in_view.strip()

        match view:
            case "1":
                #add all costs together
                total = 0.00
                for record in finances:
                    total += record["cost"]
                print(f"\nTotal Spending: ${total:.2f}\n")

            case "2":
                category = choose_exp()
                total = 0.00
                for record in finances:
                    if record["item"] == category:
                        total += record["cost"]
                print(f"\nTotal Spending for {category}: ${total:.2f}\n")

            case "3":
                print("Enter the date range (MM/DD/YYYY - MM/DD/YYYY): ")
            
            case "4":
                print("\nCancelled.\n")
            case _:
                print("\nInvalid choice, please try again.\n")


    elif choice == "4":
        print ("Goodbye!")
        break #This breaks the while loop and ends it

    elif choice == "5":
        df = pd.DataFrame(finances)
        print(df.head())

    else:
        print("Invalid choice, please try again.")