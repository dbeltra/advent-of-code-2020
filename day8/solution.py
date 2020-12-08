
def parse_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def find_solutions(data):
    part_1 = find_solution_1(data)
    part_2 = find_solution_2(data)
    return part_1, part_2

def find_solution_1(data):
    line_position = acc = 0
    exit_program = False
    executed_lines = []
    while not exit_program:
        if line_position not in executed_lines:
            executed_lines.append(line_position)
            command, argument = get_instruction(line_position, data)
            line_position, acc = run_instruction(command, argument, line_position, acc, data)
        else:
            exit_program = True
    return acc

def find_solution_2(data):
    line_position = acc = 0
    exit_program = False
    executed_lines = []
    changed_instructions = []
    current_attempt = 1

    while not exit_program:
        if line_position not in executed_lines:
            executed_lines.append(line_position)
            command, argument = get_instruction(line_position, data)

            if len(changed_instructions) < current_attempt:
                if line_position not in changed_instructions:
                    if command != 'acc':
                        changed_instructions.append(line_position)
                        if command == 'jmp':
                            command = 'nop'
                        elif command == 'nop':
                            command = 'jmp'

            line_position, acc = run_instruction(command, argument, line_position, acc, data)

            if line_position >= len(data):
                exit_program = True

        else:
            line_position = acc = 0
            executed_lines = []
            current_attempt += 1

    return acc

def get_instruction(line_position, data):
    command = data[line_position].split(' ')[0]
    argument = int(data[line_position].split(' ')[1])
    return command, argument

def run_instruction(command, argument, line_position, acc, data):
    if command == 'jmp':
        line_position += argument
    else:
        line_position += 1
        if command == 'acc':
            acc += argument

    return line_position, acc


if __name__ == "__main__":
    data = parse_file('input.txt')
    solution1, solution2 = find_solutions(data)
    print(f'SOLUTION1: {solution1}, SOLUTION2: {solution2}')
