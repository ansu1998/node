print("Welcome to the Budget App")
budget = float(input("Please enter your initial budget: "))
expenses = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add an expense")
    print("2. Show budget details")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        expenses.append({"description": description, "amount": amount})
        print(f"Added expense: {description}, Amount: {amount}")
    elif choice == "2":
        print(f"\nTotal Budget: {budget}")
        print("Expenses:")
        total_expenses = sum(expense['amount'] for expense in expenses)
        for expense in expenses:
            print(f"- {expense['description']}: {expense['amount']}")
        print(f"Total Spent: {total_expenses}")
        print(f"Remaining Budget: {budget - total_expenses}")
    elif choice == "3":
        print("Exiting Budget App. Goodbye!")
        break
    else:
        print("Invalid choice, please choose again.")
