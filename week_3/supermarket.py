items = ["Fanta", "Bread", "Milk", "Pillow", "Pan"] 

sales = [
    {"name":"King", "item": "Bread"},
    {"name":"Peter", "item": "Milk"}
]


print(f"{"==" * 24}\nHi, Welcome to Moku Supermaket\n{"==" * 24}")
name = input("Please tell us your name: ")
user_item = input(f"Hello {name}. What do you want to buy?\n{items}\nWrite the name of what you want: ")


if user_item in items:
    option = input(f"You selected {user_item}. Do you want to go ahead and buy this product?\n(Choose Yes/No):")

    if option == "Yes":
        sales.append({"name":name, "item": user_item})
        print("Thank you. Have a nice a day.")
    elif option == "No":
        print("I'm sorry we were not able to satisfy your want. Have a nice a day.")
    else:
        print("You choose the wrong option. Is either Yes or No")
        
else:
    print("Sorry. We don't have that in store")


print(sales)
