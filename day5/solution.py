
MAX_ROWS = 128
MAX_COLS = 8

def divide_subset(minseat, maxseat, charseat):
    seatspan = (maxseat - minseat)/2
    if charseat in ['L','F']:
        maxseat = minseat + seatspan
    if charseat in ['R', 'B']:
        minseat = maxseat - seatspan
    return minseat, maxseat


def find_row(boardingpass):
    rowchars = boardingpass[:7]
    minrow = 0
    maxrow = MAX_ROWS
    for charrow in rowchars:
        minrow, maxrow = divide_subset(minrow, maxrow, charrow)
    return int(minrow)


def find_col(boardingpass):
    colchars = boardingpass[-3:]
    mincol = 0
    maxcol = MAX_COLS
    for charcol in colchars:
        mincol, maxcol = divide_subset(mincol, maxcol, charcol)
    return int(mincol)

def get_seat_id(row, col):
    return row * 8 + col

def init_plane():
    plane = []
    for r in range(MAX_ROWS):
        col = ['O' for c in range(MAX_COLS)]
        plane.append(col)
    return plane

def show_plane(plane):
    print('    |   0    1    2    3    4    5    6    7')
    print('-----------------------------------------------')
    for rnumber, row in enumerate(plane):
        print(f"{rnumber:03d} | {str(row)}")
    print('-----------------------------------------------')
    print('    |   0    1    2    3    4    5    6    7')


def get_empty_seats(plane):
    empty_seats = []
    for rnumber, row in enumerate(plane):
        for colnumber, seat in enumerate(row):
            if seat == 'O':
                empty_seats.append((rnumber, colnumber))

    return empty_seats

def get_seat_with_adjacents(empty_seats, plane):
    for seat in empty_seats:
        row = seat[0]
        col = seat[1]
        try:
            in_front = plane[row-1][col]
            behind = plane[row-1][col]

            if in_front != 'O' and behind != 'O':
                return (row,col)
        except IndexError:
            pass

    return None


def find_solution(data):
    plane = init_plane()
    max_seat_id = 0
    for boardingpass in data:
        row = find_row(boardingpass)
        col = find_col(boardingpass)
        seat_id = get_seat_id(row,col)

        plane[row][col] = 'X'

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print(f'MAX ID found {max_seat_id}')
    show_plane(plane)

    empty_seats = get_empty_seats(plane)

    solution = get_seat_with_adjacents(empty_seats, plane)

    return get_seat_id(solution[0], solution[1])

def file_to_list(filename):
    with open(filename, 'r') as file:
        data = list(file.read().splitlines())
    return data

if __name__ == "__main__":
    data = file_to_list('input.txt')
    solution = find_solution(data)
    print(f'SOLUTION: {solution}')
