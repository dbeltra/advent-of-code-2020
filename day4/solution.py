import re

def parse_dict(data):
    parsed_elements = []
    for element in data:
        elem_dict = {}
        dataset = element.split(' ')
        for data in dataset:
            id_pair = data.split(':')
            elem_dict[id_pair[0]] = id_pair[1]
        parsed_elements.append(elem_dict)

    return parsed_elements

def validate_number(number, minval, maxval):
    if number > maxval or number < minval:
        return False
    return True

def validate_height(height_data):
    unit = height_data[-2:]
    if unit != 'in' and unit != 'cm':
        return False
    height = int(height_data[:-2])
    if unit == 'cm':
        if not validate_number(height, 150, 193):
            return False
    if unit == 'in':
        if not validate_number(height, 59, 76):
            return False
    return True

def find_solution(data):
    data = parse_dict(data)
    mandatory_data = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = []
    invalid_passports = []

    for passport in data:
        has_all_fields = True
        for field in mandatory_data:
            if field not in passport:
                has_all_fields = False
                break

        if has_all_fields:
            all_fields_valid = True
            byr = int(passport['byr'])
            if not validate_number(byr, 1920, 2002):
                all_fields_valid = False

            iyr = int(passport['iyr'])
            if not validate_number(iyr, 2010, 2020):
                all_fields_valid = False

            eyr = int(passport['eyr'])
            if not validate_number(eyr, 2020, 2030):
                all_fields_valid = False

            hgt = passport['hgt']
            if not validate_height(hgt):
                all_fields_valid = False

            hcl = passport['hcl']
            match = re.search('#[0-9,a-z]{6}', hcl)
            if not match:
                all_fields_valid = False

            ecl = passport['ecl']
            options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if not ecl in options:
                all_fields_valid = False

            pid = passport['pid']
            match = re.search('[0-9]{9}', pid)
            if not match:
                all_fields_valid = False

            if all_fields_valid:
                valid_passports.append(passport)
            else:
                invalid_passports.append(passport)


    return len(valid_passports)

def file_to_list(filename):
    data = []
    buffer = ''
    with open(filename, 'r') as file:
        for line in file:
            buffer += line.replace("\n", "") + ' '
            if line == '\n':
                data.append(buffer.rstrip())
                buffer = ''

    return data

if __name__ == "__main__":
    data = file_to_list('input.txt')
    solution = find_solution(data)
    print(f'SOLUTION: {solution}')
