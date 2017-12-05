from random import *

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

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
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Uderstanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        extra_insanity = randint(0, 1)
        if extra_insanity:
            print("The insanity rots your eyes into a pool of muck.")
            print("Good job!")
        else:
            print("You win Cthulhu's prized El Camino!")
            print("You speed off into the sunset....")
            exit()

else:
    print("You stumble around and fall on a knife and die. Good job!")
