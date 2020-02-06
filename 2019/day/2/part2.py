# Day 2: 1202 Program Alarm Part 1
# https://adventofcode.com/2019/day/2

from part1 import execute_intcode


if __name__ == "__main__":
        attempt = 1
        result_code = 0
        scope = 85
        for noun in range(1, scope):
            for verb in range(1, scope):
                if result_code != 19690720:
                    with open('day/2/input.txt', 'r') as input_raw:
                        instruction_set = [list(map(int, instruction_set_raw.split(','))) for instruction_set_raw in input_raw][0]
                        instruction_set[1] = noun
                        instruction_set[2] = verb
                        result_code = execute_intcode(instruction_set)
                        print("Attempt #" + str(attempt) + "  Noun: " + str(noun) + "  Verb: " + str(verb) + "  Result Code: " + str(result_code))
                        attempt += 1
                else:
                    print("Answer: " + str(((100 * noun) + verb) - 1))
                    exit()
