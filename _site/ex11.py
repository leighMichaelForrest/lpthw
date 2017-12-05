output_string = "So you're {} old, {} tall, and {} heavy."
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print(output_string.format(age, height, weight))

next_output_string = "So you live in {}, and your favourite brew is {}."
city = input("What city do you live in?")
beer = input("What is your desert island beer?")

print(next_output_string.format(city, beer))
