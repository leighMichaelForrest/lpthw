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
    def __init__(self):
        self.enemies = []

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


class ToxicSwamp(Scene):
    def __init__(self):
        super(Scene, self).__init__()
        self.treasure = 'elixir'

    def enter(self, hero):
        print(dedent("""You are in the toxic swamp."""))

        if hero.has_item('amulet'):
            print("You are immune to the toxic swamp. You make it to the shore.")
        else:
            index = 10

            while index > 0:
                factor = randint(0,5)
                if factor == 0:
                    print("You advance")
                    index -= factor
                else:
                    print("The hero has been attacked by the swamp.")
                    hero.defeat(factor)

                # determine if hero is dead
                if hero.alive():
                    continue
                else:
                    return 'dead'

        while True:
            print("A door appears.")
            if self.treasure:
                print("A bottle of elixir is beside the door.")
            print("What is your choice?")
            choice = input("> ")
            # there is an elixir. hero can take it.
            if choice == "take elixir" and self.treasure:
                hero.add_inventory(self.treasure)
                print(f"{hero.name} takes {self.treasure}")
                self.treasure = None
            elif choice == "open door":
                return 'dragon'
        else:
            print("Make a valid choice.")


class Atrium(EnemyRoom):

    def __init__(self):
        super(EnemyRoom, self).__init__()
        self.enemy = Character("Frankie", 1)
        self.treasure = 'elixir'

    def enter(self, hero):
        print(dedent("""You are in the Atrium."""))

        if self.enemy:
            print("Frankie is in the room.")
        else:
            print("Frankie has been neutralized.")

        while True:
            choice = input("Enter your choice\n> ")

            # if choice is attack, hero dies
            if choice == "attack":
                return 'dead'
            # if choice is piledrive frankie, hero dies
            elif choice == "piledrive frankie" and self.enemy:
                print("Frankie crushes your skull with the greatest of ease.")
                return 'dead'
            # if choice is confuse frankie, he is neutralized
            elif choice == "confuse frankie" and self.enemy:
                print("Frankie is slumped into a corner.")
                print("A bottle of elixir appears.")
                self.enemy = None
            elif choice == "open door right":
                if self.enemy:
                    print(f"{self.enemy} guards the door.")
                    continue
                else:
                    return 'spider'
            elif choice == "open door left":
                if self.enemy:
                    print(f"{self.enemy} guards the door.")
                    continue
                else:
                    return 'fred'
            elif choice == "take elixir" and not self.enemy and self.treasure:
                hero.add_inventory(self.treasure)
                print(f"{hero.name} takes {self.treasure}")
                self.treasure = None
            else:
                print("Make a valid choice.")


class FredsLair(EnemyRoom):

    def __init__(self):
        super(EnemyRoom, self).__init__()
        self.enemy = Character("Fred", 6)
        self.treasure = 'small ruby'

    def enter(self, hero):
        print(dedent("""You are in the Fred's Lair."""))

        if self.enemy:
            print("Fred is in the room.")
        else:
            print("Fred has been neutralized.")

        while True:
            choice = input("Enter your choice\n> ")

            # if choice is attack, battle
            if choice == "attack":
                # if Fred is neutralized, continue
                if not self.enemy:
                    print("Fred has been neutralized.")
                    continue
                else:
                    self.fight(hero, self.enemy)

                # Check if current enemy and self are alive
                if not self.enemy.alive():
                        self.enemy = None
                        print(f"The {self.treasure} is available.")
                if not hero.alive():
                    return 'dead'

            # Handle door choices
            elif choice == "open door ahead":
                if self.enemy:
                    print(f"{self.enemy} guards the door.")
                    continue
                else:
                    return 'ghost_knight'
            elif choice == "open door right":
                if self.enemy:
                    print(f"{self.enemy} guards the door.")
                    continue
                else:
                    return 'spider'
            elif choice == "go back":
                return 'atrium'
            # handle treasure
            # if enemies are killed, hero can take treasure
            elif choice == f'take {self.treasure}':
                if not self.enemy:
                    print(f"You take {self.treasure}.")
                    hero.add_inventory(self.treasure)
                    self.treasure = None
                    continue
                else:
                    print(f"You must kill {self.enemy} to take the {self.treasure}.")
            else:
                print("Make a valid choice.")


class DragonRoom(EnemyRoom):

    def __init__(self):
        super(EnemyRoom, self).__init__()
        self.enemy = Character("Dragon", 25)

    def enter(self, hero):

        # To enter, you must posess the amulet, halberd, and the ruby
        if (
            hero.has_item('amulet') and hero.has_item('small ruby')
            and hero.has_item('halberd')
        ):
            print(dedent("""You are in the Dragon Room. There is no way out. You
            either kill the dragon or you die."""))
        else:
            print("You must have the halberd, the small ruby, and the amulet to enter.")
            return 'atrium'

        while True:
            # dragon has 50/50 chance of attacking
            if randint(0,1) == 1:
                print(f"{self.enemy} attacks!")
                self.fight(self.enemy, hero)

            # in dragon room, print out stats in each iteration
            print(f"{hero.name}: {hero.strength}")
            print(f"{self.enemy}: {self.enemy.strength}")
            choice = input("Enter your choice\n> ")

            # if choice is attack, battle
            if choice == "attack":
                self.fight(hero, self.enemy)

                # Check if enemy and self are alive
                if not self.enemy.alive():
                    print("The dragon has been vanquished!\n\n\n")
                    return 'finished'
                if not hero.alive():
                    return 'dead'

            elif choice == "drink elixir":
                if hero.drink_elixir():
                    print(f"{hero.name} drinks the elixir. Strength is now 20.")
                else:
                    print(f"{hero.name} has no elixir.")
            else:
                print("Make a valid choice.")



class SpiderRoom(EnemiesRoom):
    """Room filled with spiders. Subclasses EnemiesRoom."""
    def __init__(self):
        super(EnemiesRoom, self).__init__()
        self.enemies = []
        # first add ten spiders
        for i in range(5):
            self.add_enemy('spider', 2)

        self.treasure = 'amulet'

    def enter(self, hero):
        # empty enemy variable
        enemy = None

        # print the text
        print(dedent("""You are in the spider room!"""))
        print(f"There are {len(self.enemies)} spiders.")
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
                    print(f"You must kill enemies to take the {self.treasure}.")

            # if choice is either the door left or forward, the enemies must
            # be destroyed
            elif choice == "open door ahead":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'toxic_swamp'
            elif choice == "open door left":
                    if self.enemies:
                        print("The enemies must be defeated before opening door.")
                    else:
                        return 'fred'

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
                    print(f"{self.treasure} is in the room.")
                else:
                    pass
            else:
                print("Make a valid choice.")


class GhostKnightRoom(EnemiesRoom):
    """Room filled with ghost knights. Subclasses EnemiesRoom."""
    def __init__(self):
        super(EnemiesRoom, self).__init__()
        self.enemies = []
        # first add ten spiders
        for i in range(1):
            self.add_enemy('ghost knight', 5)

        self.treasure = 'halberd'

    def enter(self, hero):
        # empty enemy variable
        enemy = None

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
                    print("You must kill enemies to take {self.treasure}.")

            # if choice is either the door left or forward, the enemies must
            # be destroyed
            elif choice == "open door behind":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'fred'

            elif choice == "open door right":
                if self.enemies:
                    print("The enemies must be defeated before opening door.")
                else:
                    return 'toxic_swamp'
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
    hero.add_inventory('amulet')
    # hero.add_inventory('halberd')
    # hero.add_inventory('small ruby')
    atrium = ToxicSwamp()
    print(atrium.enter(hero))
    #print(atrium.enter(hero))
