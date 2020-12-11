from itertools import product
import copy

def parse_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def check_seats(data:list, max_neighbours:int, count_empty:bool) -> int:
    seats_changed = True

    while seats_changed:
        new_arrangement = copy.deepcopy(data)
        seats_changed = False

        for nrow, row in enumerate(data):
            for ncol, seat in enumerate(row):
                if seat != '.':
                    adjacents_occupied = get_adjacents(nrow, ncol, count_empty, data)
                    if seat == 'L':
                        if adjacents_occupied == 0:
                            new_arrangement[nrow][ncol] = '#'
                            seats_changed = True
                    elif seat == '#':
                        if adjacents_occupied >= max_neighbours:
                            new_arrangement[nrow][ncol] = 'L'
                            seats_changed = True

        data = copy.deepcopy(new_arrangement)

    occupied = sum(row.count('#') for row in data)
    return(occupied)

def get_adjacents(row:int, col:int, count_empty:bool, data:list) -> int:
    adjacents_occupied = 0

    for direction in range(8):
        neighbour, coordinates = check_neighbour(row, col, direction, data)
        if not count_empty:
            while neighbour == '.':
                neighbour, coordinates = check_neighbour(coordinates[0], coordinates[1], direction, data)
        if neighbour == '#':
            adjacents_occupied += 1

    return adjacents_occupied

def check_neighbour(row:int , col:int, direction:int, data:list):
    adjacent_directions = list(product([-1,0,1], repeat=2))
    adjacent_directions.remove((0,0))
    directions = adjacent_directions[direction]
    if 0 <= (row + directions[0]) < len(data) and 0 <= (col + directions[1]) < len(data[0]):
        return data[row + directions[0]][col + directions[1]], (row + directions[0], col + directions[1])
    else:
        return None, None #out of boundaries

if __name__ == "__main__":
    data = parse_file('input.txt')
    solution1 = check_seats(data, 4, True)
    solution2 = check_seats(data, 5, False)
    print(f'SOLUTION1: {solution1}, SOLUTION2: {solution2}')
