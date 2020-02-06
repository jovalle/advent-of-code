import math


""" Calculate mass of module using rocket equation """
def calculate_mass(module):
    mass = int(module)
    mass /= 3
    mass = math.floor(mass)
    mass -= 2
    return mass


""" Calculate sum of fuel as per mass """
def calculate_fuel(module, fuel=0):
    # get initial mass
    mass = calculate_mass(module)
    fuel += mass

    # iterate through possible fuel requirements
    while mass > 0:
        staged_mass = calculate_mass(mass)
        # if mass is greater than 0, continue recursion and add to sum
        if staged_mass > 0:
            mass = staged_mass
            fuel += mass
        else:
            break

    return fuel


if __name__ == "__main__":
    with open('day1.txt', 'r') as modules:
        sum = 0
        for module in modules:
            sum += calculate_fuel(module)
        print(sum)
