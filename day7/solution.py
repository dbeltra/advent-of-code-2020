import re

def file_to_list(filename):
    with open(filename, 'r') as file:
        data = [line.strip() for line in file]
    return data

def find_solutions(data):
    bags = parse_bags_data(data)
    part_1 = find_containers_for('shiny gold', bags)
    part_2 = find_content_for('shiny gold', bags)

    return part_1, part_2

def parse_bags_data(data):
    bags = {}
    for rule in data:
        bag_type = rule.split('bags contain')[0].strip()
        bags[bag_type] = None
        content = rule.split('contain')[1]
        pattern = '(\d)\s(\w+\s\w+)'

        result = re.findall(pattern, content)
        if result:
            bags[bag_type] = []
            for item in result:
                bags[bag_type].append({
                    'units': int(item[0]),
                    'type': item[1],
                })
    return bags

def find_containers_for(type_of_bag, bags, found=[]):
    containers = []
    for bag in bags:
        if bags[bag]:
            for item in bags[bag]:
                if item['type'] == type_of_bag:
                    containers.append(bag)

    if len(containers) > 0:
        for container in containers:
            if container not in found:
                found.append(container)
        for type_of_bag in containers:
            find_containers_for(type_of_bag, bags)

    return len(found)


def find_content_for(type_of_bag, bags):
    content = bags[type_of_bag]
    if content is None:
        return 0
    else:
        total_in_bag = 0
        for bag in content:
            bags_in_this_bag = find_content_for(bag['type'], bags)
            total_in_bag += bag['units'] + (bag['units'] * bags_in_this_bag)

        return total_in_bag

if __name__ == "__main__":
    data = file_to_list('input.txt')
    solution1, solution2 = find_solutions(data)
    print(f'SOLUTION1: {solution1}, SOLUTION2: {solution2}')
