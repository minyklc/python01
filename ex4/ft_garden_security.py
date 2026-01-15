#!/usr/bin/env python3
class Plant:

    '''the same class plant with plant's data and behavior'''

    def __init__(self, name: str, height: int, age: int):
        self.a1 = name
        self._a2 = height
        self._a3 = age

    def get_info(self):
        print(f"{self.a1}: {self.a2:.0f}cm, {self.a3} days old")

    def age(self):
        self._a3 += 1

    def grow(self, length: int):
        self._a2 += length
        return (length)


class SecurePlant:

    '''SecurePlant class to protect data by creating methods
       getter/setter'''

    def __init__(self, plant: Plant):
        self.plant = plant

    '''getter method with @property that returns the data wanted, the height'''
    @property
    def height(self):
        return self.plant._a2

    '''setter method with the name of the method affected with @property
       followed by .setter, to assign a new value to an attributes'''
    @height.setter
    def height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.plant._a2 = height
            print(f"Height updated: {self.plant._a2}cm [OK]")

    '''getter for the plant's age'''
    @property
    def age(self):
        return self.plant._a3

    '''setter of the age, for both setters, if the new value is negative,
       it is rejected and prints an error message'''
    @age.setter
    def age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.plant._a3 = age
            print(f"Age updated: {self.plant._a3} days [OK]")


def main():
    '''envelop the Plant variable by the Secure class to add the security
       and use getter/setter in SecurePlant'''
    print("=== Garden Security System ===")
    rose = SecurePlant(Plant("Rose", 20, 25))
    name = rose.plant.a1
    print(f"Plant created: {name}")
    rose.height = 25
    rose.age = 30
    print("")
    rose.height = -5
    print("")
    print(f"Current plant: {name} "
          f"({rose.height}cm, {rose.age} days)")


if __name__ == "__main__":
    main()
