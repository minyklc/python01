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
    print("=== Garden Management System Demo ===\n")


if __name__ == "__main__":
    main()
