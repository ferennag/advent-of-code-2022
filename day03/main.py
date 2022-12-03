def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return list(map(lambda line: line.strip(), lines))

def to_char_array(input: str):
    return [ch for ch in input]

def common_items(rucksack: str):
    n = len(rucksack)
    first = set(to_char_array(rucksack[0:n//2]))
    second = set(to_char_array(rucksack[n//2:]))

    return list(first.intersection(second))

def priority(item: chr):
    if item.isupper():
        return 27 + ord(item) - ord('A')
    else:
        return 1 + ord(item) - ord('a')

def group_input(rucksacks: [str]):
    result = []
    for i in range(0, len(rucksacks), 3):
        single_group = [rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]]
        result.append(single_group)
    return result

def find_common_item(group: [str]):
    result = list(map(lambda g: set(g), group))
    return list(result[0].intersection(result[1].intersection(result[2])))


def main():
    input = read_input('input1.txt')

    result = 0
    for rucksack in input:
        priorities = list(map(priority, common_items(rucksack)))
        result = result + sum(priorities)
    
    print('1.: %d' % result)

    groups = group_input(input)
    print('2.: %d' % sum(map(lambda g: priority(find_common_item(g)[0]), groups)))

if __name__ == '__main__':
    main()