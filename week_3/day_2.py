# LOOP
# Is a block of code that keeps on running until a condition is met.

num = 0

# while num < 10:
#     print(num)
#     num = num + 1


# people = ["John", "Peter", "Ade", "Oluadamilare", "king"]

# searched_name = input("Who are you looking for: ")

# for person in people:
#     if person == searched_name:
#         print(f"Person found: {person}")
#         break # Stops the loop
# else: # Runs the the loop has stopped
#     print("The person you are looking for is not found.")


# numbers = [1,2,3,4,5,6,7,8,9,10]
# updated_num = []

# for num in numbers:
#     num = num * 2
#     updated_num.append(num)
# else:
#     print("NUMBERS:", numbers)
#     print("UPDATED NUMBERS:",updated_num)


# first_num = [1,2,3,4,5]
# second_num = [6,7,8,9,10]

# for num in second_num:
#     first_num.append(num)
# else:
#     print(first_num)

people = ["John", "Peter", "Ade", "Oluadamilare", "king"]
# email_users = []

# for person in people:
#     # Concatenation
#     email_address = person + "@mail.com"

#     email_users.append(email_address)
# else:
#     print(email_users)


name = input("Who are you looking for?: ").strip()

for person in people:
    if name.lower() == person.lower():
        print(name)
        people.remove(person)
        print(f"{person} removed.")
        break
else:
    print("This person is not in the list")




