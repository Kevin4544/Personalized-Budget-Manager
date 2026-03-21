import datetime
# This file will hold methods related to finances, based on the input from main

spending_types = ["Groceries", "Rent", "Utilities", "Entertainment",
                  "Savings Transfer", "Emergency Fund", "Other"]

class Account:

    def __init__(self):
        #finances is a list made of dictionaries
        self.finances = []

    def choose_expense(self):
        
        # For loop just to show the options for types of spending
        count = 1
        print()
        for item in spending_types:
            print(f"{count}. {item}")
            count += 1
        print("8. Cancel\n") #This one is separate since "cancel" isn't a type of spending, the list is useful for later

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
            case "5":
                return "Savings Transfer"
            case "6": 
                return "Emergency Fund"
            case "7":
                exp = input("Enter the name of the expense: ")
                return exp
            case "8":
                print("\nCancelled.\n")
                return -1
            case _:
                print("\nInvalid choice, please try again.")
                return None
                

    def add_expense(self, exp_type, cost):
        row_test = {"Spending Type": exp_type, "Cost": cost, "Date": datetime.datetime.now().strftime("%m/%d/%Y")}
        self.finances.append(row_test)
        print(f"\nStored: {exp_type} for ${cost:.2f}")

    def expense_list(self):
        return self.finances

    def see_balance(self):
        print("1. All expenses \n2. By category \n3. By date \n4. Cancel\n")
        
        in_view = input("Enter your choice: ")
        view = in_view.strip()

        match view:
            case "1":
                #add all costs together
                total = 0.00
                for record in self.finances:
                    total += record["Cost"]
                print(f"\nTotal Spending: ${total:.2f}")

            case "2":
                category = self.choose_expense()

                # Currently does not work
                total = 0.00
                for record in self.finances:
                    if record["category"] == category:
                        total += record["Cost"]
                print(f"\nTotal Spending for {category}: ${total:.2f}\n")

            case "3":
                print("Enter the date range (MM/DD/YYYY - MM/DD/YYYY): ")
            
            case "4":
                print("\nCancelled.\n")
            case _:
                print("\nInvalid choice, please try again.\n")