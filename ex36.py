from random import randint
from textwrap import dedent


def start():
    """The start of the game."""
    print(dedent("""
    You are in a pure white atrium with two doors. In your pocket is
    a dagger. Which door do you choose? The one on the right or the one on the left?
    """))

    choice = input('> ')

    if choice == "left":
        spider_room()
    elif choice == "right":
        gorgon_room()
    else:
        dead("Die!")
        exit()


def dead(why):
    """Kill the application when the player dies."""
    print(why, "Good Job!")
    exit(0)


def spider_room():
    """Player goes against giant spiders using randomly generated numbers (2-12)"""
    # player lives
    player = 6
    # number of spiders
    spiders = 12

    print(dedent(
    """You are in a dark room with jagged granite walls. From all corners come
    12 giant spiders who aren't just hungry....
    THEY ARE HANGRY!!!!!!\n\n"""))

    while player > 0 and spiders > 0:
        player_roll = randint(2, 12)
        spider_roll = randint(2, 12)

        if player_roll > spider_roll:
            spiders_killed = randint(1, spiders)
            print(f"{spiders_killed} spiders killed!")
            spiders -= spiders_killed
        else:
            print("You are wounded!")
            player -= 1

    if player > 0:
        print("You killed the spiders.\n\n\n")
        toxic_swamp()
    else:
        dead("You have been killed by giant spiders!")


def gold_room():
    """Print out the victory text."""
    print(dedent("""
You are in a bright room with Italian marble floor to ceiling.
You have found the gold.\n\n\n
    """))
    exit()


def toxic_swamp(amulet=False):
    """Player either walks across a toxic swamp, goes back home, or
    is killed in the muck. Twelve steps. At random, the swamp takes
    a bit of the player's life. If amulet is worn, he makes it to
    the other side."""
    player = 6
    print("Player sees a toxic swamp.")
    print("Do you advance or retreat?")
    choice = input("> ")

    if choice == "retreat":
        start()
    elif choice == "advance":
        print("You have chosen to traverse the swamp.")
    else:
        dead("You did not make a choice!")

    # if you make it to this point, you cross the swamp at your peril
    if amulet:
        print("You are immune to the swamp's toxic burn!")
    else:
        for step in range(1, 13):
            toxicity = randint(0,1)
            print(f"step :{step}")

            if toxicity:
                print("You are attacked!")
                player -= 1
            else:
                print("You advance!")

            # if player is at zero in the loop, die
            if not player:
                dead("You have been killed in the toxic swamp!")

    # if you made it this far, you advance
    print("You have made it across the swamp.")

    # make a new choice
    print("There are two passages: one on the left and one to the right")

    while True:
        print("Which one do you wish to take?")

        choice = input("> ")

        if choice == "right":
            cave()
        elif choice == "left":
            dragons_lair()
        else:
            print("Make a choice!")


def gorgon_room():
    """Room is guarded by a gorgon. If player succeeds in taking a mirror
    player has a chance a picking up the amulet. If player does not take
    mirror, player could turn to stone."""
    amulet = False

    print("A door is guarded by a hideous gorgon. A mirror is at your feet.")
    print("Do you pick up the mirror?")

    choice = input("> ")

    if choice == "pick up mirror":
        print("Gorgon sees it image and turns to stone.")
        print("By the door, there is an amulet.")
    elif choice == "go back":
        start()
    else:
        dead("Player turns to stone.")

    while True:
        print("What do you do now?")

        choice = input("> ")

        if choice == "take amulet":
            amulet = True
        elif choice == "open door":
            break
        else:
            print("Make a choice.")

    toxic_swamp(amulet)


def dragons_lair(wand=False):
    """Fight the dragon. Room functions like a 3-dice attack in
    the classic board game Risk. Dragon has at most 3 dice. Player
    has at most two."""
    player_lives = 6
    dragon_lives = 10

    print("You have entered the dragon's lair.")

    while True:
        print("What do you wish to do. Fight or flee?")

        choice = input("> ")

        if choice == "fight":

            dragon_rolls = dice_roll(dragon_lives, True)
            player_rolls = dice_roll(player_lives)

            # determine number of iterations
            if len(player_rolls) <= len(dragon_rolls):
                roll_iterations = player_rolls
            else:
                roll_iterations = dragon_rolls

            for index, roll in enumerate(roll_iterations):
                # add one to the value if player has wand
                if wand:
                    player_rolls[index] += 1
                else:
                    pass

                # determine who wins the die roll
                if player_rolls[index] >= dragon_rolls[index]:
                    dragon_lives -= 1
                    print("You got a shot on the dragon.")
                elif player_rolls[index] < dragon_rolls[index]:
                    player_lives -= 1
                    print("The dragon's breath burned you.")
                else:
                    print("uhhhh")
                    continue

                # player or dragon dies when they reach zero
                if player_lives <=0:
                    dead("The dragon burned you up.")
                elif dragon_lives <= 0:
                    print("\a\a\a\a\aYou have killed the dragon!")
                    gold_room()
                else:
                    continue
        elif choice == "flee":
            start()
        else:
            print("Make a choice!")


def dice_roll(lives, dragon=False):
    """Return a list containing sorted dice rolls. If dragon is
    true, there will be at most 3 rolls."""
    rolls = []
    number_of_rolls = 0

    # determine number of rolls for dragon or player.
    if lives >= 4 and dragon:
        number_of_rolls = 3
    elif lives >= 3:
        number_of_rolls = 2
    else:
        number_of_rolls = 1


    # roll dice and append
    for roll in range(number_of_rolls):
        face_number = randint(1,6)
        rolls.append(face_number)

    # # return sorted list (descended)
    return sorted(rolls, reverse=True)


def cave():
    print("You are in a granite cave.")
    print("In the center of the room, there is a magic wand placed on a velvet pillow.")

    print("What do you choose?")

    choice = input("> ")

    if choice == "take wand":
        dragons_lair(True)
    else:
        print("You advance to the dragon's lair without an advantage.")
        dragons_lair()


# The driver function
start()
