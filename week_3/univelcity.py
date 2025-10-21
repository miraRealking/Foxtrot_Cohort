ui_ux_design = []
front_end_developement = []
backend_development = []


print("Welcome to Univelcity.")
name = input("What is your name?: ")
course = input(f"What course are you planning to take?\n1. UI/UX Design.\n2. Front-End Development\n3. Back-End Development.\n(Choose one 1/2/3): ")


if course == "1":
   ui_ux_design.append(name)
elif course == "2":
   front_end_developement.append(name)
elif course == "3":
   backend_development.append(name)
else:
   print("You choose the wrong option. You are to choose between 1, 2 or 3.")


print("UI\\UX Design:", ui_ux_design)
print("Front-End Development:", front_end_developement)
print("Backend Development:", backend_development)

