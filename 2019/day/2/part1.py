# Day 2: 1202 Program Alarm Part 1
# https://adventofcode.com/2019/day/2

def execute_intcode(iset):
    """ Run through sequence of opcodes and parameters as per Intcode program specs """

    position = 0  # keep track of logical position
    index = 0     # keep track of literal position

    # iterate through all instructions
    for i in iset:

        # ensure logical and literal positions are in sync
        if index == position:

            # get position targets
            x = int(iset[index + 1])
            y = int(iset[index + 2])
            z = int(iset[index + 3])

            # desync positioning to "step" forward
            position = index + 4

            try:
                if i == 1:
                    iset[z] = str(int(iset[x]) + int(iset[y]))
                elif i == 2:
                    iset[z] = str(int(iset[x]) * int(iset[y]))
                elif i == 99:
                    break
            except IndexError:
                continue

        # keep track of literal position
        index += 1

    return iset[0]


if __name__ == "__main__":
    with open('day/2/input.txt', 'r') as input_raw:
        instruction_set = [list(map(int, instruction_set_raw.split(','))) for instruction_set_raw in input_raw][0]

        # restore gravity assist program
        instruction_set[1] = 12
        instruction_set[2] = 2

        print(execute_intcode(instruction_set))
