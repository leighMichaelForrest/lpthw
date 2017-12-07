from sys import exit
from random import randint
from textwrap import dedent

class Character(object):
    """The object representing the player."""
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def factor(self, attacker=False):
        """Return an integer based on character strength and offense."""
        if self.strength > 3 and attacker:
            factor = 3
        elif self.strength > 2:
            factor = 2
        else:
            factor = 1

        return factor

    def attack_dice(self, factor):
        """Return a reverse sorted array of integers between 1 and 6."""
        dice = []
        for i in range(factor):
            dice.append(randint(1,6))

        return sorted(dice,reverse=True)

    def battle(self, opponent):
        """Initiate a battle. Opponent is on defense."""
        # set factor to 3 if greater than 3
        character_factor = self.factor(True)
        opponent_factor = opponent.factor(False)

        # get the attack dice
        character_dice = self.attack_dice(character_factor)
        opponent_dice = self.attack_dice(opponent_factor)

        min_number = min(len(character_dice), len(opponent_dice))

        # run the battle
        for idx, val in enumerate(range(min_number)):
            if character_dice[idx] > opponent_dice[idx]:
                opponent.defeat(1)
                print(opponent.name, "loses")
            else:
                self.defeat(1)
                print(opponent.name, "wins")

    def defeat(self, factor):
        """Deduct the right amount of strength."""
        self.strength -= factor

    def alive(self):
        """Returns true if strength is a positive integer greater than 0."""
        return self.strength > 0

    def __str__(self):
        """String representation of the Character."""
        return f"{self.name}"

class Enemy(Character):
    pass


class Hero(Character):
    def __init__(self, name, strength):
        """Construct  Hero object."""
        super(Character, self).__init__()
        self.name = name
        self.strength = strength
        self.inventory = []

    def add_inventory(self, treasure):
        """Add item to inventory. All that is needed is a string."""
        self.inventory.append(treasure)

    def has_item(self, item):
        """Return true if item is in inventory"""
        if item in self.inventory:
            return True
        else:
            return False

    def drink_elixir(self):
        if self.has_item('elixir'):
            self.strength = 20
            return True
        else:
            return False

    def __str__(self):
        """String representing the Hero."""
        str_1 = ""
        str_1 += self.name
        str_1 += "items:\n"

        for item in self.inventory:
            str_1 += item + '\n'

        return str_1
