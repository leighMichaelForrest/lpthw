from random import *

print("""You enter a dark room with two doors.
Do you go through door #1, door #2, or #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Rub the bear's belly.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("There is a dark lake surrounded by caverns on its shores.")
    print("A BIG KRAKEN IS RELEASED!!!!!")
    print("What do you do?")
    print("1. Stare at the Kraken.")
    print("2. Pull out a mirror and show it.")
    print("3. Throw a huge rock at the beast.")

    insanity = input(">")

    if insanity == "1" or insanity == "3":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        mirror_power = randint(0, 1)
        if extra_insanity:
            print("The Kraken turns to stone!")
            print("You win the grand and glorious jackpot!")
        else:
            print("The Kraken's roar shatters the mirror.")
            print("The Kraken proceeds to crush you underfoot.")
            print("Good Job!")

elif door == "3":
    print("""
There are a large number of spiders coming out of many crevices.
Do you:
    1. Fight
    2. Flee""")

    action = input("> ")

    if action == "1":
        print("A giant spider emerges and eats your innards.")
        print("Good Job.")
    else:
        print("A rock drops from the ceiling and crushes you.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
