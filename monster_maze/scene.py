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

    def fight(self, character, enemy):
        """Initialize a battle. character is not necessarily a Hero,
        but can be an enemy."""
        character.battle(enemy)


class EnemiesRoom(Scene):
    """Class for a roomful of enemies."""
    def __init__(self, treasure):
        super(Scene, self).__init__()
        self.enemies = []
        self.treasure = treasure

    def fight(self, character, enemy):
        character.battle(enemy)

    def add_enemy(self, name, strength):
        enemy = Enemy(name, strength)
        self.enemies.append(enemy)


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


class SpiderRoom(EnemiesRoom):
    def enter(self, hero):
        # empty enemy variable
        enemy = None

        # first add ten spiders
        for i in range(5):
            self.add_enemy('spider', 2)

        # print the text
        print(dedent("""You are in the spider room!"""))
        print(self.enemies)

        # Action loop
        while True:
            # initialize spider
            # if the enemies list is empty, set it to None
            if  self.enemies:
                enemy = self.enemies[0]
            else:
                enemy = None

            #50/50 chance of spiders attacking; spider must exist
            if enemy is not None and randint(0,1) == 1:
                print("Spider attacks!")
                self.fight(enemy, hero)

            # get the choice
            choice = input("What is your choice?\n> ")

            # if enemies are killed, hero can take treasure
            if choice == f'take {self.treasure}':
                if not self.enemies:
                    print(f"You take {self.treasure}.")
                    hero.add_inventory(self.treasure)
                    self.treasure = None
                    continue
                else:
                    print("You must kill enemies to take the amulet.")

            # if choice is either the door left or forward, the enemies must
            # be destroyed
            elif choice == "open door ahead":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'finished'

            elif choice == "open door left":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'finished'
            # the option to go back is always available
            elif choice == "go back":
                return 'atrium'
            elif choice == "attack":
                # if there are no spiders, continue
                if not self.enemies:
                    print("There are no spiders to attack.")
                    continue
                else:
                    self.fight(hero, enemy)

                # Check if current enemy and self are alive
                if not enemy.alive():
                    del self.enemies[0]
                if not hero.alive():
                    return 'dead'
                # after attack print the number of spiders left
                if self.enemies:
                    print(f"There are {len(self.enemies)} left.")
                elif not self.enemies and self.treasure:
                    print("The amulet is in the room.")
                else:
                    pass
            else:
                print("Make a valid choice.")


class GhostKnightRoom(EnemiesRoom):
    def enter(self, hero):
        # empty enemy variable
        enemy = None

        # first add 5 ghost knights
        for i in range(1):
            self.add_enemy('Ghost Knight', 5)

        # print the text
        print(dedent("""You are in the Ghost Knight room!"""))

        # Action loop
        while True:
            # initialize ghost knight
            # if the enemies list is empty, set it to None
            if  self.enemies:
                enemy = self.enemies[0]
            else:
                enemy = None

            #50/50 chance of ghost knight attacking; ghost knight must exist
            if enemy is not None and randint(0,1) == 1:
                print(f"{enemy} attacks!")
                self.fight(enemy, hero)

            # get the choice
            choice = input("What is your choice?\n> ")

            # if enemies are killed, hero can take treasure
            if choice == f'take {self.treasure}':
                if not self.enemies:
                    print(f"You take {self.treasure}.")
                    hero.add_inventory(self.treasure)
                    self.treasure = None
                    continue
                else:
                    print("You must kill enemies to take the amulet.")

            # if choice is either the door left or forward, the enemies must
            # be destroyed
            elif choice == "open door behind":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'finished'

            elif choice == "open door right":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'finished'
            # the option to go back is always available
            elif choice == "go back":
                return 'atrium'
            elif choice == "attack":
                # if there are no ghost knights, continue
                if not self.enemies:
                    print("There are no enemies to attack.")
                    continue
                else:
                    self.fight(hero, enemy)

                # Check if current enemy and self are alive
                if not enemy.alive():
                    del self.enemies[0]
                if not hero.alive():
                    return 'dead'
                # after attack print the number of spiders left
                if self.enemies:
                    print(f"There are {len(self.enemies)} left.")
                elif not self.enemies and self.treasure:
                    print(f"The {self.treasure} is in the room.")
                else:
                    pass
            else:
                print("Make a valid choice.")


if __name__ == '__main__':
    hero = Hero("Leigh",12)
    spider_room = GhostKnightRoom('large ruby')
    print(spider_room.enter(hero))
