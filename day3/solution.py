def check_coordinates(data, row, col):
    row = data[row]
    if col >= len(row):
        col = col % len(row)

    elem = row[col]

    if elem == '#':
        return 'tree'
    else:
        return 'space'

def check_slope(data, right, down):
    ntrees = 0
    row = 0
    col = 0

    while row < len(data):
        result = check_coordinates(data, row, col)
        if result == 'tree':
            ntrees += 1

        row += down
        col += right

    return ntrees

def find_solution(data):
    ntrees = check_slope(data, 3,1)
    return ntrees


def find_solution_2(data):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    ntrees = 1
    for slope in slopes:
        slopetrees = check_slope(data, slope[0], slope[1])
        ntrees = ntrees * slopetrees
    return ntrees


def file_to_list(filename):
    with open(filename, 'r') as file:
        data = list(file.read().splitlines())
    return data

if __name__ == "__main__":
    data = file_to_list('input.txt')
    solution = find_solution_2(data)
    print(solution)
