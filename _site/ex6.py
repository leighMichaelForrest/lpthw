# initialize types_of_people to 10
types_of_people = 10
# initialize x to a formatted string, types_of_people being inserted into it.
x = f"There are {types_of_people} types of people."

# initialize binary to the string "binary"
binary = "binary"
# initialize do_not to the string "don't"
do_not = "don't"
# initialize y to the formatted string "Those who know binary and those who don't"
#    note: "binary" and "don't" are inserted where the variable names are
#    in the curly braces.
y = f"Those who know {binary} and those who {do_not}"

# Write the formatted string x
print(x)
# Write the formatted string y
print(y)

# Write to the screen "I said {x}", x being the formatted string x.
print(f'I said: "{x}"')
# Write to the screen "I also said {y}", y being the formatted string y.
print(f"I also said: '{y}'")

# initialize hilarious to False, a boolean value.
hilarious = True
# Initialize joke_evaluation to a string with curly braces in it.
joke_evaluation = "Isn't that joke so funny?! {}"

# Print joke_evaluation with the value of hilarious injected where the
#    curly braces are.
print(joke_evaluation.format(hilarious))

# initialize w to "This is the left side of..."
w = "This is the left side of..."
# initialize e to "a string with a right side."
e = "a string with a right side."

# concatenate e to w.
print(w + e)
