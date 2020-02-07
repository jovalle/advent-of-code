# Day 1: The Tyranny of the Rocket Equation Part 1
# https://adventofcode.com/2019/day/1
import os
import sys

def calculate_mass(m):
    """Calculate mass of module using rocket equation"""
    return int(m) // 3 - 2


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], 'input.txt'), 'r') as modules:
        masses = [ calculate_mass(int(mass)) for mass in modules ]
        print(sum(masses))
