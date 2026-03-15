import financer


def choose_method():
    print("\nWhich budgeting method would you like to use?")
    print("1. 50/30/20 Rule \n2. Zero-based \n3. Envelope \n4. 70/20/10 Rule \n5. Cancel\n")

    in_method = input("Enter your choice: ")
    method = in_method.strip()

    match method:
        case "1":
            #fifty_thirty_twenty()
            pass
        case "2":
            #zero_based()
            pass
        case "3":
            #envelope()
            pass
        case "4":
            #seventy_twenty_ten()
            pass
        case "5":
            print("\nCancelled.\n")
        case _:
            print("\nInvalid choice, please try again.\n")

#Budgeting methods
def fifty_thirty_twenty():
    pass

def zero_based():
    pass

def envelope():
    # Limited amounts for each expense category
    pass

def seventy_twenty_ten():
    pass







