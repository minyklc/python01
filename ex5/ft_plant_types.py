#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.a1 = name
        self.a2 = height
        self.a3 = age

    def get_info(self):
        print(f"{self.a1}: {self.a2:.0f}cm, {self.a3} days old")

    def age(self):
        self.a3 += 1

    def grow(self, length):
        self.a2 += length
        return (length)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.a4 = color

    def bloom(self):
        return f"{self.a1} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.a4 = trunk_diameter

    def produce_shade(self, nb):
        return f"{self.a1} provides {nb} square meters of shade"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.a4 = harvest_season
        self.a5 = nutritional_value


def main():
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.a1} ({rose.__class__.__name__}): "
          f"{rose.a2}cm, {rose.a3} days, {rose.a4} color")
    print(f"{rose.bloom()}\n")

    tulip = Flower("Tulip", 20, 39, "red")
    print(f"{tulip.a1} ({tulip.__class__.__name__}): "
          f"{tulip.a2}cm, {tulip.a3} days, {tulip.a4} color")
    print(f"{tulip.bloom()}\n")

    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.a1} ({oak.__class__.__name__}): "
          f"{oak.a2}cm, {oak.a3} days, {oak.a4}cm diameter")
    print(f"{oak.produce_shade(78)}\n")

    sakura = Tree("Sakura", 475, 1250, 100)
    print(f"{sakura.a1} ({sakura.__class__.__name__}): "
          f"{sakura.a2}cm, {sakura.a3} days, {sakura.a4}cm diameter")
    print(f"{sakura.produce_shade(90)}\n")

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"{tomato.a1} ({tomato.__class__.__name__}): "
          f"{tomato.a2}cm, {tomato.a3} days, {tomato.a4} harvest")
    print(f"{tomato.a1} is rich in {tomato.a5}\n")

    carrot = Vegetable("Carrot", 30, 70, "spring", "vitamin A")
    print(f"{carrot.a1} ({carrot.__class__.__name__}): "
          f"{carrot.a2}cm, {carrot.a3} days, {carrot.a4} harvest")
    print(f"{carrot.a1} is rich in {carrot.a5}\n")


if __name__ == "__main__":
    main()
