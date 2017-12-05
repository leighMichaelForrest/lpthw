# Declare a function with cheese_count and boxes_of_crackers as arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print out what's in cheese_count arguments
    print(f"You have {cheese_count} cheeses!")
    # print out what's in boxes_of_crackers arguement
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # write "Man, that's enough for a party!" to the screen
    print("Man, that's enough for a party!")
    # write "Get a blanket
    # " to the screen.
    print("Get a blanket\n")


# write "We can just give the function numbers directly:"
print("We can just give the funtion numbers directly:")
# run cheese_and_crackers with 20 cheeses and 30 boxes of crackers
cheese_and_crackers(20, 30)


# write "OR, we can use variables from our script:"
print("OR, we can use variables from our script:")
# set amount_of_cheese to 10
amount_of_cheese = 10
# set amount_of_crackers to 50
amount_of_crackers = 50

# run cheese_and_crackers with amount_of_cheese and amount_of_crackers variables,
#    respectively.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# write "We can even do math inside too:" to the screen.
print("We can even do math inside too:")
# call cheese_and_crackers with the formulae 10 + 20 and 5 + 6, respectively
cheese_and_crackers(10 + 20, 5 + 6)


# write "And we can combine the two, variables and math:"
print("And we can combine the two, variables and math:")
# call cheese_and_crackers with amount_of_cheese + 100 and
#   amount_of_crackers + 1000, respectively
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def barley_and_hops(bags_of_barley, cones_of_hops):
    print(f"You have {bags_of_barley} bags of barley and  {cones_of_hops} hops.")
    print("That is enough to brew some beer.\n")

barley_bags = 15
hop_cones = 25

barley_and_hops(barley_bags, hop_cones)
barley_and_hops(10, 4)
barley_and_hops(10 - 2, 4 - 1)
barley_and_hops(10 + 2, 4 + 1)
barley_and_hops(barley_bags + 100, hop_cones + 100)
barley_and_hops(barley_bags - 5, hop_cones - 5)
barley_and_hops(barley_bags, hop_cones + 4)
barley_and_hops(barley_bags + 5, hop_cones)
barley_and_hops(barley_bags, hop_cones - 4)
barley_and_hops(barley_bags - 1, hop_cones)
