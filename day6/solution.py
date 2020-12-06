def find_solution(data):
    return sum(len(list(set(answer_group.replace(' ','')))) for answer_group in data)

def find_solution_2(data):
    result = 0
    for answer_group in data:
        for idx, person_answer in enumerate(answer_group.split(' ')):
            if idx > 0:
                common_yes = set(person_answer).intersection(common_yes)
            else:
                common_yes = set(person_answer)
        result += len(list(common_yes))
    return result

def file_to_list(filename):
    data = []
    buffer = ''
    with open(filename, 'r') as file:
        for line in file:
            if line == '\n':
                data.append(buffer.strip())
                buffer = ''
            else:
                buffer = f'{buffer} {line.strip()}'
        data.append(buffer.strip())

    return data

if __name__ == "__main__":
    data = file_to_list('input.txt')
    solution = find_solution_2(data)
    print(f'SOLUTION: {solution}')
