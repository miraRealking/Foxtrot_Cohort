# ------------Tracker program-----------------
# 1. Create a list called expenses. It's going to be a list of dictionary in this format e.g [{"expense": "Transportation", "price": 400}].

print(f"{"===" * 7}\nTracker Program\n{"===" * 7}")

expenses = [
            {"expense": "Transportation", "price": 400},
            {"expense": "Food", "price": 200},
            {"expense": "Rent", "price": 1000}
]


while True:
    expense_name = input("Write the expense name: ")
    expense_price = float(input("Write the price: "))

    # 2 Create a dictionary with the keys and values of expense and price
    new_expense = {
        "expense": expense_name,
        "price": expense_price
    }

    # 4 Define your budget limit
    budget_limit = 600

    # 4. Write an if else statement. If price is greater than (put your price), update the dictionary with the key # # "is_over_the_budget", set True and append to expenses.


    if expense_price > budget_limit:
        new_expense ["is_over_the_budget"] = True
    else:
        new_expense["is_over_the_budget"] = False

    # Append the new_expense to the expenses list
    expenses.append(new_expense)

    print(f"{expense_name} has been added.")


    option = input("Do you want to continue?(Choose y/n): ")

    if option == "y":
        continue
    elif option == "n":
        for item in expenses:
            print(f"Expense: {item["expense"]}, Price: {expense_price}")
        break
    else:
        print("Invalid option")