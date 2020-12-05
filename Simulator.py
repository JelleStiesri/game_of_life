from copy import deepcopy

from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        self.prevWorld = deepcopy(self.world)  # Maakt een copy van de vorige wereld

        for x in range(self.world.width):
            for y in range(self.world.height):

                total_neigbours = np.count_nonzero(self.prevWorld.get_neighbours(x, y))  # Geeft het aantal levende buren

                if self.prevWorld.get(x, y) == 1: # Als de cel nog leeft
                    if total_neigbours == 2 or total_neigbours == 3:
                        self.world.set(x, y)
                    else:
                        self.world.set(x, y, 0)
                else: # Als de cel al dood is
                    if total_neigbours == 3:
                        self.world.set(x, y, 1)
                    else:
                        self.world.set(x, y, 0)

        return self.world


    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world

