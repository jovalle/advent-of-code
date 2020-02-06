import math


if __name__ == "__main__":
    with open('day1.txt', 'r') as modules:
        sum = 0
        for module in modules:
            mass = int(module)
            mass /= 3
            mass = math.floor(mass)
            mass -= 2
            sum += mass
        print(sum)
