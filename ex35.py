from sys import exit
from textwrap import dedent
from random import randint

def gold_room():
    """A room with gold in it."""

    print("This room is full of gold. How much do you take?")

    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            dead("Man, learn to type a number.")
        else:
            if choice < 50:
                print("Nice, you're not greedy, you win!")
                exit(0)
            else:
                dead("You greedy bastard!")


def bear_room():
    print(dedent("""
    There is a bear here.
    The bear has a bunch of honey
    The fat bear is in front of another door.
    How are you going to move the bear?
    """))
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt_bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    """Room with a cthulhu."""

    print(dedent("""
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?
    """))

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head " in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def spider_room():
    """The spider room. Fight the spiders with randomly generated numbers."""
    spiders = 12
    player = 6

    print(dedent("""
    In the dark  cavernous room emerge something creepy...
    There are now 12 GIANT HUNGRY SPIDERS!!!!!!
    They are on the attack...
    """))

    # start the play loop
    while player > 0 and spiders > 0:
        # if player wins, deduct 1 from spiders, else take one from player.
        dice_roll = roll_dice()

        if dice_roll:
            spiders_killed = randint(1,spiders)
            print(f"You killed {spiders_killed} giant spiders.")
            spiders -= spiders_killed
        else:
            print("You have been wounded by a spider.")
            player -= 1
            # end while loop

    if player > spiders:
        print("The spiders have been killed. Open the door if you dare.")
    else:
        dead("You have been killed by the horde of giant spiders.")

    while True:
        choice = input("> ")

        if choice == "open door":
            gold_room()
        elif choice == "go back":
            start()
        else:
            print("I got no idea what that means.")


def roll_dice():
    """True if player greater than spiders. Else false."""
    player = randint(2, 12)
    spiders = randint(2, 12)

    if player > spiders:
        return True
    else:
        return False

def dead(why):
    """The death function."""
    print(why, "Good job!")
    exit(0)

def start():
    """The starting chamber of the game."""
    print(dedent("""
    You are in a dark room.
    There is a door to your right, to the center, and left.
    Which one do you take?
    """))

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "center":
        spider_room()
    else:
        dead("You stumble around the room until you starve.")


start()
