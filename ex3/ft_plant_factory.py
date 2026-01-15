#!/usr/bin/env python3
class Plant:
    '''same class Plant'''
    def __init__(self, name: str, height: int, age: int):
        self.a1 = name
        self.a2 = height
        self.a3 = age

    '''info on a plant'''
    def get_info(self):
        print(f"{self.a1}: {self.a2:.0f}cm, {self.a3} days old")

    '''add 1 day when age is called'''
    def age(self):
        self.a3 += 1

    '''add lenght when grow is called'''
    def grow(self, length: int):
        self.a2 += length
        return (length)


def main():

    '''this is the factory part, where all the datas are
       organized in a list'''

    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    garden = []
    nb = 0

    print("=== Plant Factory Output ===")

    '''for each plant and their datas, a plant is created and then append
       in garden, an another list that contains plants created with Plant'''

    for plant in data:
        actual = Plant(*plant)
        garden.append(actual)
        print(f"Created: {actual.a1} ({actual.a2}cm, {actual.a3} days)")
        nb += 1
    print(f"\nTotal plants created: {nb}")


if __name__ == "__main__":
    main()
