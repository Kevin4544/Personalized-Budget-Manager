import finance


inny = input("Would you like to begin using a budgeting method? (y/n)")
if inny.lower() == "y":
    print("\nWhich budgeting method would you like to use?")
    print("1. 50/30/20 Rule \n2. Zero-based \n3. Envelope \n4. 70/20/10 Rule \n5. Cancel\n")
    
    in_method = input("Enter your choice: ")
    method = in_method.strip()

    match method:
        case "1":
            finance.fifty_thirty_twenty()
        case "2":
            finance.zero_based()
        case "3":
            finance.envelope()
        case "4":
            finance.seventy_twenty_ten()
        case "5":
            print("\nCancelled.\n")
        case _:
            print("\nInvalid choice, please try again.\n")

#Budgeting methods

# 50% on needs, 30% on wants, 20% on savings/debt repayment
def fifty_thirty_twenty():
    pass

def zero_based():
    pass

def envelope():
    pass

def seventy_twenty_ten():
    pass







