test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

with open('src/inputs/day3_input.txt', 'r', encoding='utf-8') as text:
    actual = text.read()
rucksacks = actual.splitlines()


def char_to_priority(char: str):
    char_code = ord(char)
    if char_code < 91:
        priority = char_code - 65 + 27
        return priority
    priority = char_code - 97 + 1
    return priority


total_p1 = 0
for rucksack in rucksacks:
    comp_1, comp_2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    [common] = list(set(comp_1).intersection(comp_2))
    total_p1 += char_to_priority(common)

print(total_p1)

total_p2 = 0
groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
for group in groups:
    [rucksack1, rucksack2, rucksack3] = group
    [common] = list(set(rucksack1).intersection(rucksack2).intersection(rucksack3))
    total_p2 += char_to_priority(common)

print(total_p2)
