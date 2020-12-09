from itertools import combinations

def parse_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def find_solution_1(data: list) -> int:
    preamble = 25
    for idx, number in enumerate(data[preamble:], preamble):
        preamble_list = data[idx-preamble:idx]
        valid_pair = False
        for pair in list(combinations(preamble_list, 2)):
            if pair[0] + pair[1] == number:
                valid_pair = True
                break
        if not valid_pair:
            return number

def find_solution_2(data: list, target_number: int) -> int:
    start = index = 0
    candidates = []
    solved = False
    while not solved:
        candidates.append(data[index])
        if sum(candidates) == target_number and data[index] != target_number:
            solved = True
        if sum(candidates) < target_number:
            index += 1
        if sum(candidates) > target_number:
            candidates = []
            index = start = start + 1

    candidates.sort()
    return candidates[0] + candidates[-1]

if __name__ == "__main__":
    data = parse_file('input.txt')
    solution1 = find_solution_1(data)
    solution2 = find_solution_2(data, solution1)
    print(f'SOLUTION1: {solution1}, SOLUTION2:{solution2}')
