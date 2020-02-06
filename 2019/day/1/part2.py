# Day 1: The Tyranny of the Rocket Equation Part 2
# https://adventofcode.com/2019/day/1

from part1 import calculate_mass


def calculate_fuel(module, fuel=0):
    """ Calculate sum of fuel as per module mass """
    fuel = calculate_mass(module)
    if fuel > 0:
        # recursively calculate each fuel requirement until empty
        return fuel + calculate_fuel(fuel)
    else:
        return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as modules:
        # get sum of list of fuel requirements
        print(sum([ calculate_fuel(module) for module in modules ]))
