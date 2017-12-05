from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
user_input = input("What would you like to print on the screen? ")
print(f"The user says: \"{user_input}\"")
