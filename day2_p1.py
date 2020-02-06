import csv


if __name__ == "__main__":
    with open('day2.txt', 'r') as instruction_set_raw:
        # [] to unpack double list output
        [instruction_set] = list(csv.reader(instruction_set_raw))
        print(instruction_set)

        # restore gravity assist program
        instruction_set[1] = str(12)
        instruction_set[2] = str(2)

        position = 0  # keep track of logical position
        index = 0     # keep track of literal position

        for instruction in instruction_set:
            opcode = int(instruction)
            print(opcode)

            # ensure logical and literal positions are in sync
            if index == position:

                # get position targets
                x = int(instruction_set[index + 1])
                y = int(instruction_set[index + 2])
                z = int(instruction_set[index + 3])

                # desync positioning to "step" forward
                position = index + 4

                if opcode == 1:
                    instruction_set[z] = str(int(instruction_set[x]) + int(instruction_set[y]))
                    print("ADD: @Pos:" + str(x) + " (" + instruction_set[x] + ") + @Pos:" + str(y) + " (" + instruction_set[y] + ") = " + instruction_set[z])
                elif opcode == 2:
                    instruction_set[z] = str(int(instruction_set[x]) * int(instruction_set[y]))
                    print("MULTIPLY: @Pos:" + str(x) + " (" + instruction_set[x] + ") * @Pos:" + str(y) + " (" + instruction_set[y] + ") = " + instruction_set[z])
                elif opcode == 99:
                    print("HALT")
                    break

            # keep track of literal position
            index += 1

        print("Remainder: " + instruction_set[0])
