#!usr/bin/python3

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


class SecurePlant:
    def __init__(self, plant):
        self.plant = plant

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.plant.a2 = height
            print(f"Height updated: {self.plant.a2}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.plant.a3 = age
            print(f"Age updated: {self.plant.a3} days [OK]")

    def get_height(self):
        return self.plant.a2

    def get_age(self):
        return self.plant.a3


def main():
    print("=== Garden Security System ===")
    rose = SecurePlant(Plant("Rose", 20, 25))
    name = rose.plant.a1
    print(f"Plant created: {name}")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    print("")
    print(f"Current plant: {name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    main()
