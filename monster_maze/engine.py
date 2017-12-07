from sys import exit
from random import randint
from textwrap import dedent

from character import Character, Enemy, Hero
from scene import FredsLair, Atrium, SpiderRoom, Death, \
    Finished, GhostKnightRoom, DragonRoom, ToxicSwamp


class Engine(object):
    """Class that drives the game."""

    def __init__(self, scene_map):
        """Initialize the engine with the map and the hero."""
        self.scene_map = scene_map
        self.hero = Hero('Leigh', 12)

    def play(self):
        """Play the game."""
        current_scene = self.scene_map.opening_scene()
        last_scene =  self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.hero)
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter(self.hero)


class Map(object):


    scenes = {
        'atrium': Atrium(),
        'fred': FredsLair(),
        'spider': SpiderRoom(),
        'toxic_swamp': ToxicSwamp(),
        'ghost_knight': GhostKnightRoom(),
        'dragon': DragonRoom(),
        'dead': Death(),
        'finished':Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        """Return the next scene."""
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        """Return the scene that starts the game."""
        return self.next_scene(self.start_scene)


if __name__ == '__main__':
    a_map = Map('atrium')
    a_game = Engine(a_map)
    a_game.play()
