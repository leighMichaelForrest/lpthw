from sys import exit
from random import randint
from textwrap import dedent

from character import Character, Enemy, Hero


class Scene(object):
    """Generic Scene class. Objects must override the enter() method,
    with a Hero object being passed into it."""

    def enter(self, hero):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)


class EnemyRoom(Scene):
    """Generic class with a single enemy."""
    pass


    def fight(self, character, enemy):
        """Initialize a battle. character is not necessarily a Hero,
        but can be an enemy."""
        character.battle(enemy)


class EnemiesRoom(Scene):
    """Class for a roomful of enemies."""
    def __init__(self, treasure):
        super(Scene, self).__init__()
        self.treasure = treasure

    def fight(self, character, enemy):
        character.battle(enemy)


class FredsLair(EnemyRoom):
    """The scene where the hero battles Fred the Ogre."""
    def __init__(self):
        super(EnemyRoom, self).__init__()

        self.enemy = Enemy('Fred', 5)
        self.treasure = 'amulet'

    def enter(self, hero):
        print(dedent("""
        The room has bare wooden walls with high windows.
        In the background creeps a huge humanoid figure. It's
        Fred the Ogre! Look Out!
        """))

        if self.enemy is None:
            print("You advance!")
            return 'ghost_knights'

        print("In the room is an enemy: ", self.enemy)

        while True:
            # 50/50 attempt of enemy starting fight
            attacked = randint(0,1)
            if self.enemy and attacked == 1:
                print(self.enemy, "attacks!")
                self.fight(self.enemy, hero)

            # determine input
            print("What would you like to do?")
            choice = input("> ")
            if choice == 'attack':
                self.fight(hero, self.enemy)

                if not self.enemy.alive():
                    print("enemy is dead.")
                    self.enemy = None
                elif not hero.alive():
                    return 'dead'
                else:
                    continue
            elif choice == 'open door' and not self.enemy:
                    return 'ghost_knights'
            elif choice == 'open door' and self.enemy:
                    print("You must defeat Fred to advance.")
                    continue
            elif choice == 'take amulet' and not self.enemy:
                # get the treasure
                hero.add_inventory(self.treasure)
                print(f"You take the {self.treasure}")
            elif choice == 'take amulet' and self.enemy:
                print("You must defeat Fred to take the amulet.")
            else:
                return 'atrium'


class SpiderRoom(EnemiesRoom):
    def __init__(self):
        """Initialize MinionsRoom with enemies and treasure."""
        super(EnemiesRoom, self).__init__()

        self.enemies = []
        self.treasure = 'magic wand'
        # initialize the minions
        for _ in range(10):
            enemy = Enemy('spider', 2)
            self.enemies.append(enemy)

    def enter(self, hero):
        """The overridden enter() method."""
        print(dedent("""
            You have entered a room with dark granite faces on all four walls.
            A glowing fire emanates from the center
        """))

        if not self.enemies:
            print("You advance!")
            return 'fountain'

        print(f"In the room are {len(self.enemies)} spiders. ")

        enemy = self.enemies.pop()

        while True:
            print(f"Hero's stamina:{hero.strength}")
            if enemy is None:
                enemy = self.enemies.pop()

            # 50/50 attempt of enemy starting fight
            attacked = randint(0,1)
            if attacked == 1:
                print(enemy, "attacks!")
                self.fight(enemy, hero)

            # determine input
            print("What would you like to do?")
            choice = input("> ")
            if choice == 'attack':
                self.fight(hero, enemy)

                if not enemy.alive():
                    print("enemy is dead.")
                    enemy = None
                if len(self.enemies) == 0:
                    break
                elif not hero.alive():
                    return 'dead'
                else:
                    print(f"There are {len(self.enemies)} left.")
                    continue

            else:
                return 'atrium'

        hero.add_inventory(self.treasure)
        print(f"You take the {self.treasure}")

        return 'fountain'


class GhostKnightsRoom(EnemiesRoom):
    def __init__(self):
        """Initialize MinionsRoom with enemies and treasure."""
        super(EnemiesRoom, self).__init__()

        self.enemies = []
        self.treasure = 'giant ruby'
        # initialize the minions
        for _ in range(10):
            enemy = Enemy('ghost knight', 5)
            self.enemies.append(enemy)

    def enter(self, hero):
        """The overridden enter() method."""
        print(dedent("""
            The Ghost Knight Room!
        """))

        if self.enemies is None:
            print("You advance!")
            return 'finished'

        print(f"In the room are {len(self.enemies)} ghost knights. ")
        while len(self.enemies) > 0:
            print(f"There are {len(self.enemies)} left.")
            enemy = self.enemies.pop()
            # 50/50 attempt of enemy starting fight
            attacked = randint(0,1)
            if attacked == 1:
                print(enemy, "attacks!")
                self.fight(enemy, hero)

            # determine input
            print("What would you like to do?")
            choice = input("> ")
            if choice == 'attack':
                self.fight(hero, enemy)

                if not enemy.alive():
                    print("enemy is dead.")
                elif not hero.alive():
                    return 'dead'
                else:
                    continue

            else:
                return 'atrium'

        hero.add_inventory(self.treasure)
        print(f"You take the {self.treasure}")

        return 'finished'


class MinorTreasureRoom(Scene):
    """Scene that contains the minor treasure."""
    def __init__(self):
        self.treasure = "minor treasure"

    def enter(self, hero):
        # make sure the player has the amulet and the magic wand
        if not hero.has_item("magic wand") and not hero.has_item("amulet"):
            print("You cannot enter the room.")
            return 'atrium'
        else:
            print(dedent("""
            You have entered the the wooden room of the minor treasure,
            a small chest with gilt corners.
            """))

            while True:
                print("What do you choose?")
                choice = input("> ")

                if choice == "take treasure":
                    hero.add_inventory("minor treasure")
                elif choice == "exit":
                        return 'atrium'
                else:
                    print("Make a choice!")

class Atrium(Scene):
    def enter(self, hero):
        print(dedent("""You are in a white room, with three doors. Each one
        is marked with a number."""))

        while True:
            choice = input("> ")

            if choice == "open door 1":
                print("You chose door 1")
                return 'fred'
            elif choice == "open door 2":
                print("You chose door 2")
                return 'minor_treasure'
            elif choice == "open door 3":
                print("You chose door 3")
                return 'spiders'


class MagicFountain(Scene):
    def __init__(self):
        self.drinks = 3

    def enter(self, hero):
        print(dedent("""You have entered the room with the magic fountain."""))

        # There are four choices: go to the door ahead, go to the door behind,
        # drink from the fountain, and stay here
        while True:
            print("What is your choice?")
            choice = input("> ")

            if choice == "drink from fountain":
                if self.drinks < 1:
                    return "The fountain has run dry."
                else:
                    hero.drink_from_fountain()
                    self.drinks -= 1
            elif choice == "open door behind":
                return 'spiders'
            elif choice == "open door ahead":
                return  'toxic_swamp'
            else:
                print("Make a choice!")


class ToxicSwamp(Scene):
    def enter(self, hero):
        print(dedent("""You have entered the toxic swamp."""))
        return 'dragon'


class DragonRoom(EnemyRoom):
    """The scene where the hero battles the dreaded dragon."""
    def __init__(self):
        super(EnemyRoom, self).__init__()

        self.enemy = Enemy('THE DRAGON', 25)

    def enter(self, hero):
        print(dedent("""
        DRAGON ROOM
        """))

        if not hero.dragon_qualified():
            print("You need all four treasures to enter.")
            return 'atrium'

        print("In the room is your main enemy: ", self.enemy)

        while True:
            # 50/50 attempt of enemy starting fight
            attacked = randint(0,1)
            if self.enemy and attacked == 1:
                print(self.enemy, "attacks!")
                self.fight(self.enemy, hero)

            # determine input
            print("What would you like to do?")
            choice = input("> ")
            if choice == 'attack':
                self.fight(hero, self.enemy)

                if not self.enemy.alive():
                    print("enemy is dead.")
                    self.enemy = None
                elif not hero.alive():
                    return 'dead'
                else:
                    continue
            elif choice == 'retreat':
                    print("You go back to the Atrium.")
                    return 'atrium'
            else:
                return 'atrium'


class Finished(Scene):
    def enter(self, hero):
        print('Fin')
        return 'finished'


class Death(Scene):
    quips = [
        "You died. You kind of suck at this.",
        "Your mom would be proud... if she were smarter.",
        "You're such a luser",
        "I have a small puppy that would be better at this.",
        "You are worse than your dad's jokes."
    ]

    def enter(self, hero):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
