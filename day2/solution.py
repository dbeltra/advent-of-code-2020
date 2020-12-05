
def find_solution(data):
    numvalid = 0
    for test_input in data:
        prange = test_input.split(' ')[0]
        minchars = int(prange.split('-')[0])
        maxchars = int(prange.split('-')[1])
        pchar = test_input.split(' ')[1].replace(':','')
        passw = test_input.split(' ')[2]

        nchars = 0
        for c in passw:
            if c == pchar:
                nchars += 1

        if nchars >= minchars and nchars <= maxchars:
           numvalid += 1

    return numvalid



def find_solution_2(data):
    numvalid = 0
    for test_input in data:
        prange = test_input.split(' ')[0]
        pos1 = int(prange.split('-')[0]) - 1
        pos2 = int(prange.split('-')[1]) -1
        pchar = test_input.split(' ')[1].replace(':','')
        passw = test_input.split(' ')[2]

        if passw[pos1] == pchar and passw[pos2] != pchar:
            numvalid +=1

        if passw[pos2] == pchar and passw[pos1] != pchar:
            numvalid +=1


    return numvalid

def file_to_list(filename):
    with open(filename, 'r') as file:
        data = list(file.read().splitlines())
    return data


if __name__ == "__main__":
    data = file_to_list('input.txt')

    solution = find_solution_2(data)
    print(solution)
