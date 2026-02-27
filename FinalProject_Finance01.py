#Initialize an empty list to store a list of the user's finances.
finances = []

print("Hello! Welcome to your Personal Finance Tracker.")

#Main loop starts here
while True:
    print("What would you like to do?")
    print("1. Add an expense")
    print("2. View an expense")
    print("3. Check total balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        #This is where the data is collected from the user
        item = input("What did you buy? ")
        cost = float(input("How much did it cost? "))

        # Store as a dictionary and add to our list
        entry = {"item": item, "cost": cost}
        finances.append(entry)
        print(f"Stored: {item} for ${cost:.2f}")

    elif choice == "2":
        print("\nExpense List")
        #A 'for' loop to iterate through our list
        for record in finances:
            print(f"*{record['item']}: ${record['cost']:.2f}")

    elif choice == "3":
        #Use a loop or sum function to calculate total
        total = 0
        for record in finances:
            total += entry["cost"]
        print(f"\nTotal Spending: ${total:.2f}")

    elif choice == "4":
        print ("Goodbye!")
        break #This breaks the while loop and ends it

    else:
        print("Invalid choice, please try again.")