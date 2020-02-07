# Day 2: 1202 Program Alarm Part 1
# https://adventofcode.com/2019/day/2
import os
import sys

def execute_intcode(intcode_set):
    """Run through sequence of opcodes and parameters as per Intcode program specs"""

    position = 0  # keep track of logical position
    index = 0     # keep track of literal position

    # iterate through all instructions
    for i in intcode_set:

        # ensure logical and literal positions are in sync
        if index == position:

            # get position targets
            x = intcode_set[index + 1]
            y = intcode_set[index + 2]
            z = intcode_set[index + 3]

            # desync positioning to "step" forward
            position = index + 4

            # check for and validate opcodes, ignore out of bound position errors
            try:
                if i == 1:
                    intcode_set[z] = intcode_set[x] + intcode_set[y]
                elif i == 2:
                    intcode_set[z] = intcode_set[x] * intcode_set[y]
                elif i == 99:
                    break
            except IndexError:
                continue

        # keep track of literal position
        index += 1

    return intcode_set[0]


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], 'input.txt'), 'r') as intcode_raw:
        intcode_set = [list(map(int, intcode_set.split(','))) for intcode_set in intcode_raw][0]

        # restore gravity assist program
        intcode_set[1] = 12
        intcode_set[2] = 2

        print(str(execute_intcode(intcode_set)))
