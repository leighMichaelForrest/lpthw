people = 30
cars = 10
trucks = 40


# if there are more cars than people, print the line
if cars > people and cars < trucks:
    print("We should take the cars.")
# else if there are more people than cars, print the line
elif cars < people:
    print("We should not take the cars.")
# if cars are equal to people, print the line.
else:
    print("We can't decide.")

# if there are more trucks than cars, print the line.
if trucks > cars:
    print("That's too many trucks.")
# else if there are more cars than trucks, print the line.
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if cars and trucks are equal, print the line.
else:
    print("We still can't decide.")

# if there are more people than trucks, print the line.
if people > trucks:
    print("Alright, let's just take the trucks.")
# otherwise, print this line.
else:
    print("Fine, let's stay home then.")
