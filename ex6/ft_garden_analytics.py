#!/usr/bin/env python3

class Plant:

    '''same Plant class'''

    def __init__(self, name: str, height: int, age: int):
        self.a1 = name
        self.a2 = height
        self.a3 = age

    def get_info(self):
        print(f"{self.a1}: {self.a2:.0f}cm, {self.a3} days old")

    def age(self):
        self.a3 += 1

    def grow(self, length: int):
        self.a2 += length
        return (length)


class FloweringPlant(Plant):

    '''FloweringPlant that takes Plants attributes + flower's color
       and their state of blooming'''

    def __init__(self, name: str, height: int, age: int, type: str):
        super().__init__(name, height, age)
        self.a4 = type
        self.a5 = "not blooming"

    def blooming(self):
        self.a5 = "blooming"
        return f"({self.a5})"


class PrizeFlower(FloweringPlant):

    '''PrizeFlower that takes Flowering Plant attributes and behavior
       + the point prize associated to the flower'''

    def __init__(self, name: str, height: int,
                 age: int, type: str, prize: int):
        super().__init__(name, height, age, type)
        self.a6 = prize


class GardenManager:

    '''when GardenManager is called, a garden is created with attributes like
       the owner's name, a list where plants are stocked, and the total growth
       and the total points initiated at 0. the garden is then append to
       an all_garden list to get track of all the gardens (with @classmethod).
       GardenManager's methods can overall add plant, make plants grow & bloom.
       there's also an inner class, GardenStats'''

    all_garden = []

    def __init__(self, name: str):
        self.garden = []
        self.name = name
        self.growth = 0
        self.points = 0

    def add_plant(self, plant: Plant):
        self.garden.append(plant)
        self.points += 10
        self.points += plant.a2
        if type(plant).__name__ == "PrizeFlower":
            self.points += plant.a6
        return f"Added {plant.a1} to {self.name}'s garden"

    def all_grow(self, length: int):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.garden:
            self.growth += plant.grow(length)
            self.points += length
            print(f"{plant.a1} grew {length}cm")

    def all_bloom(self):
        for plant in self.garden:
            if isinstance(plant, FloweringPlant):
                plant.blooming()

    @property
    def stats(self):
        return GardenManager.GardenStats(self.garden)

    @classmethod
    def create_garden_network(cls, name: str):
        variable = cls(name)
        GardenManager.all_garden.append(variable)
        return variable

    class GardenStats:

        '''GardenStats is about get datas about one specific garden, or
           all of the gardens. get_plant returns all the plants of a garden
           get_added returns the number of plants in a garden,
           get_types returns the numbers of each type of plants with
           a table of ints ([0]: regular, [1]: flower [2]: prize),
           and static methods calculates numbers of gardens, total points
           and check height with all_garden from GardenManager'''

        def __init__(self, garden):
            self.garden = garden

        @property
        def get_plant(self):
            print("Plants in garden:")
            plants = ""
            for p in self.garden:
                if type(p).__name__ == "PrizeFlower":
                    plants += f"- {p.a1}: {p.a2}cm, {p.a4} ({p.a5}), " \
                                f"Prize points: {p.a6}\n"
                elif type(p).__name__ == "FloweringPlant":
                    plants += (f"- {p.a1}: {p.a2}cm, {p.a4} ({p.a5})\n")
                else:
                    plants += (f"- {p.a1}: {p.a2}cm\n")
            return plants

        @property
        def get_added(self):
            return len(self.garden)

        @property
        def get_types(self):
            types = [0, 0, 0]
            for p in self.garden:
                if type(p).__name__ == "PrizeFlower":
                    types[2] += 1
                elif type(p).__name__ == "FloweringPlant":
                    types[1] += 1
                else:
                    types[0] += 1
            return types

        @staticmethod
        def check_h():
            for garden in GardenManager.all_garden:
                for plant in garden.garden:
                    if plant.a2 < 0:
                        return False
            return True

        @staticmethod
        def points():
            result = ""
            for garden in GardenManager.all_garden:
                result += f"{garden.name}: {garden.points}"
                if garden != GardenManager.all_garden[-1]:
                    result += ", "
            return result

        @staticmethod
        def get_gardens():
            return len(GardenManager.all_garden)


def main():

    '''alice and bob's gardens are created with GardenManager,
       then plants are added, growed and bloomed'''

    print("=== Garden Management System Demo ===\n")

    alice = GardenManager.create_garden_network("Alice")
    bob = GardenManager.create_garden_network("Bob")
    bob.add_plant(FloweringPlant("Lily", 82, 60, "white flowers"))
    p = alice.add_plant
    print(f"{p(Plant("Oak Tree", 100, 500))}")
    print(f"{p(FloweringPlant("Rose", 25, 30, "red flowers"))}")
    print(f"{p(PrizeFlower("Sunflower", 50, 45, "yellow flowers", 10))}")
    print()
    alice.all_grow(1)
    alice.all_bloom()
    print()

    '''alice report is printed with @property methods from GardenStats,
       then stats of all of the gardens is printed'''

    print(f"=== {alice.name}'s Garden Report ===")

    print(f"{alice.stats.get_plant}")
    print(
        f"Plants added: {alice.stats.get_added}, "
        f"Total growth: {alice.growth}cm"
    )
    t = alice.stats.get_types
    print(f"Plant types: {t[0]} regular, "
          f"{t[1]} flowering, "
          f"{t[2]} prize flowers\n")
    print(f"Height validation test : {GardenManager.GardenStats.check_h()}")
    print(f"Garden scores - {GardenManager.GardenStats.points()}")
    print(f"Total gardens managed: {GardenManager.GardenStats.get_gardens()}")


if __name__ == "__main__":
    main()
