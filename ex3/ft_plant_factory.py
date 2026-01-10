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


def main():
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

    for plant in data:
        actual = Plant(*plant)
        garden.append(actual)
        print(f"Created: {actual.a1} ({actual.a2}cm, {actual.a3} days)")
        nb += 1
    print(f"\nTotal plants created: {nb}")


if __name__ == "__main__":
    main()
