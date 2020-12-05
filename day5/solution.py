
MAX_ROWS = 128
MAX_COLS = 8

def find_row(boardingpass):
    rowchars = boardingpass[:7]
    minrow = 0
    maxrow = MAX_ROWS
    for charrow in rowchars:
        rowspan = (maxrow - minrow)/2
        if charrow == 'F':
            minrow = minrow
            maxrow = minrow + rowspan

        if charrow == 'B':
            minrow = maxrow - rowspan
            maxrow = maxrow

    return int(minrow)


def find_col(boardingpass):
    colchars = boardingpass[3:]
    mincol = 0
    maxcol = MAX_COLS
    for charcol in colchars:
        colspan = (maxcol - mincol)/2
        if charcol == 'L':
            mincol = mincol
            maxcol = mincol + colspan

        if charcol == 'R':
            mincol = maxcol - colspan
            maxcol = maxcol

    return int(mincol)

def get_seat_id(row, col):
    return row * 8 + col

def init_plane():
    plane = []
    for r in range(MAX_ROWS):
        col = []
        for c in range(MAX_COLS):
            col.append('O')
        plane.append(col)
    return plane

def show_plane(plane):
    print('    |   0    1    2    3    4    5    6    7')
    print('-----------------------------------------------')
    nrow = 0
    for row in plane:
        print(f"{nrow:03d} | {str(row)}")
        nrow += 1
    print('-----------------------------------------------')
    print('    |   0    1    2    3    4    5    6    7')


def get_empty_seats(plane):
    empty_seats = []
    row = 0
    for r in plane:
        col = 0
        for seat in r:
            if seat == 'O':
                empty_seats.append((row, col))
            col += 1
        row += 1

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
