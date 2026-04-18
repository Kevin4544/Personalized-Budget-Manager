import financer
import model


def choose_method():
    print("\nWhich budgeting method would you like to use?")
    print("1. 50/30/20 Rule \n2. Zero-based \n3. Envelope \n4. 70/20/10 Rule \n5. Remove current method \n6. Cancel\n")

    in_method = input("Enter your choice: ")
    method = in_method.strip()
    return method

def analyze(method, monthly_income, finances):
    match method:
        case "1":
            fifty_thirty_twenty(monthly_income, finances)

        case "2":
            zero_based(monthly_income, finances)
            
        case "3":
            envelope(monthly_income, finances)
            
        case "4":
            seventy_twenty_ten(monthly_income, finances)
        
        case "5":
            print("Removed budgeting method.")

        case "6":
            print("\nCancelled.\n")
            return -1
        case _:
            print("\nInvalid choice, please try again.\n")


#Budgeting methods
def fifty_thirty_twenty(monthly_income, finances):
    # 50% for Needs, 30% for Wants, 20% for Savings

    # This dictionary holds the target/goal for how to spend our income
    limits = {"Needs": monthly_income * 0.5, "Wants": monthly_income * 0.3, "Savings": monthly_income * 0.2 }
    
    # This dictionary holds the current income totals based on the mapping from model.py
    current = {"Needs": 0, "Wants": 0, "Savings": 0}

    for item in finances:
        category = item["Spending Type"] 
        amount = item["Cost"]
        # Assign each category to need, want, or savings, (wants by default)
        bucket = model.CATEGORIES.get(category, "Wants")
        # The 3 of these are keys for the 'current' dictionary, and you add the money as the value for each key
        current[bucket] += amount

    print("50/30/20 Budgeting Plan")
    for bucket, amounts in current.items():
        limit = limits[bucket]
        status = None
        if amounts <= limit:
            status = "Good"
        else:
            status = "Budget Limit Exceeded"
        print(f"\t{bucket}: Spent ${amounts:.2f} \n\tLimit ${limit:.2f} \n\tStatus:{status}\n")

def zero_based(monthly_income, finances):
    global zb_limits
    # This method lets the user assign their own limit for each category

    if not zb_limits:
        print("Please enter how much will be assigned as the limit to each category.")
        # 'type' refers to the 'key' values in the limits dictionary, which are the category types.
        for type in financer.spending_types:
            amount = float(input(f"{type}: "))
            monthly_income -= amount
            print(f"Remaining income: ${monthly_income:.2f}")
            zb_limits[type] = amount
        
        print("\nZero-Based Budgeting Plan")
        for type, amount in zb_limits.items():
            spent = 0
            for item in finances:
                if item["Spending Type"] == type:
                    spent += item["Cost"]
            status = None
            if spent <= amount:
                status = "Good"
            else:
                status = "Budget Limit Exceeded"
            print(f"\t{type}: Spent ${spent:.2f} \n\tLimit ${amount:.2f} \n\tStatus: {status}\n")
    
    # Need 
    


def seventy_twenty_ten(monthly_income, finances):
    # This method follows the same process as 50,30,20 method
    # 70% on Needs, 10% on Wants, 20% on Savings
    limits = {"Needs": monthly_income * 0.7, "Wants": monthly_income * 0.1, "Savings": monthly_income * 0.2 }
    
    current = {"Needs": 0, "Wants": 0, "Savings": 0}

    for item in finances:
        category = item["Spending Type"] 
        amount = item["Cost"]

        bucket = model.CATEGORIES.get(category, "Wants")
        current[bucket] += amount

    print("70/20/10 Budgeting Plan")
    for bucket, amounts in current.items():
        limit = limits[bucket]
        status = None
        if amounts <= limit:
            status = "Good"
        else:
            status = "Budget Limit Exceeded"
        print(f"\t{bucket}: Spent ${amounts:.2f} \n\tLimit ${limit:.2f} \n\tStatus: {status}\n")







