#!/usr/bin/env python3
class Plant:

    '''same attributes'''
    def __init__(self, name, height, age):
        self.a1 = name
        self.a2 = height
        self.a3 = age

    '''self.a2 is approximates to the decimal for the readability'''
    def get_info(self):
        print(f"{self.a1}: {self.a2:.0f}cm, {self.a3} days old")

    '''add 1 day to the age (self.a3) of the plant when age method is called'''
    def age(self):
        self.a3 += 1

    '''add a lenght to the height (self.a2) when grow method is called'''
    def grow(self, length):
        self.a2 += length
        return (length)


def main():

    '''rose, sunflower, cactus and tulip are in a garden list'''

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    tulip = Plant("Tulip", 20, 15)
    garden = [rose, sunflower, cactus, tulip]

    '''for each plant, it simulates a week of growth
       with age and height changed followed by the summary of the growth'''

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
        print(f"Growth this week: +{grow:.0f}cm\n")


'''main called if it's the main program'''
if __name__ == "__main__":
    main()
