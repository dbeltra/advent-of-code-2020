
def find2020(data):
    for entry1 in data:
        for entry2 in data:
            for entry3 in data:
                if int(entry1) + int(entry2) + int(entry3) == 2020:
                    return int(entry1) * int(entry2) * int(entry3)



if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = list(file.read().splitlines())

    solution = find2020(data)
    print(solution)
