#!/usr/bin/python3

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


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    tulip = Plant("Tulip", 20, 15)
    garden = [rose, sunflower, cactus, tulip]

    for plant in garden:
        i = 1
        print(f"=== Day {i} ===")
        plant.get_info()
        length = (plant.a2 + 5) / plant.a3
        grow = 0
        while i < 7:
            grow += plant.grow(length)
            plant.age()
            i += 1
        print(f"=== Day {i} ===")
        plant.get_info()
        print(f"Growth this week: +{grow:.0f}cm")
        print("\n")


if __name__ == "__main__":
    main()
