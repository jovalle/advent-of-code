import csv


def calculate_intcode(instruction_set):
    position = 0  # keep track of logical position
    index = 0     # keep track of literal position

    for instruction in instruction_set:
        opcode = int(instruction)

        # ensure logical and literal positions are in sync
        if index == position:

            # get position targets
            x = int(instruction_set[index + 1])
            y = int(instruction_set[index + 2])
            z = int(instruction_set[index + 3])

            # desync positioning to "step" forward
            position = index + 4

            try:
                if opcode == 1:
                    instruction_set[z] = str(int(instruction_set[x]) + int(instruction_set[y]))
                elif opcode == 2:
                    instruction_set[z] = str(int(instruction_set[x]) * int(instruction_set[y]))
                elif opcode == 99:
                    break
            except IndexError:
                continue

        # keep track of literal position
        index += 1

    return instruction_set[0]


if __name__ == "__main__":
        attempt = 1
        remainder = 0
        scope = 100
        for noun in range(1, scope):
            for verb in range(1, scope):
                if remainder != '19690720':
                    with open('day2.txt', 'r') as raw_input:
                        [opcodes] = list(csv.reader(raw_input))
                        opcodes[1] = str(noun)
                        opcodes[2] = str(verb)
                        remainder = calculate_intcode(opcodes)
                        print("Attempt #" + str(attempt) + "  Noun: " + str(noun) + "  Verb: " + str(verb) + "  Remainder: " + remainder)
                        attempt += 1
                else:
                    print("Answer: " + str((100 * int(noun)) + int(verb) - 1))
                    exit()
