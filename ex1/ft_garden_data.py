#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.a1 = name
        self.a2 = height
        self.a3 = age

    def get_info(self):
        print(f"{self.a1}: {self.a2}cm, {self.a3} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    tulip = Plant("Tulip", 20, 15)
    garden = [rose, sunflower, cactus, tulip]
    print("=== Day 1 ===")
    for plant in garden:
        plant.get_info()
