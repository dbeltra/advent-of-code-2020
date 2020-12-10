def parse_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return sorted([int(line.strip()) for line in file])

def find_solution_1(data: list) -> int:
    part1_data = data.copy()
    current_joltage = 0
    joltage_diff = []
    while len(part1_data) > 0:
        adapter_used = part1_data.pop(0)
        joltage_diff.append(adapter_used - current_joltage)
        current_joltage = adapter_used
    return joltage_diff.count(1) * (joltage_diff.count(3)+1)

def find_solution_2(data: list):
    data_dict = {adapter:1 for adapter in [0] + data}
    for adapter in data:
        total_combinations = 0
        for joltage_diff in range(1,4):
            if adapter - joltage_diff in data_dict:
                total_combinations += data_dict[adapter-joltage_diff]
        data_dict[adapter] = total_combinations

    return data_dict[data[-1]]

if __name__ == "__main__":
    data = parse_file('input.txt')
    solution1 = find_solution_1(data)
    solution2 = find_solution_2(data)
    print(f'SOLUTION1: {solution1}, SOLUTION2: {solution2}')
