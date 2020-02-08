# Day 2: 1202 Program Alarm Pt. 2
# https://adventofcode.com/2019/day/2
import os
import sys
from program_alarm import execute_intcode

if __name__ == "__main__":

    # safeguard answers to match
    result_code = 0

    # set scope of brute force
    scope = 85

    # brute force result with nested for loop to check all possible combinations
    for noun in range(1, scope):
        for verb in range(1, scope):
            # check result_code in previous iteration
            # if result_code is what we are looking for, print and exit on next iteration
            if result_code != 19690720:
                with open(os.path.join(sys.path[0], 'input.txt'), 'r') as intcode_raw:
                    intcode_set = [list(map(int, intcode_set.split(','))) for intcode_set in intcode_raw][0]
                    intcode_set[1] = noun
                    intcode_set[2] = verb
                    result_code = execute_intcode(intcode_set)
            else:
                print(str(((100 * noun) + verb) - 1))
                exit()
