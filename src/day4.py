test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

with open('src/inputs/day4_input.txt', 'r', encoding='utf-8') as text:
    actual = text.read()
pairs = actual.splitlines()


def get_range_ints_from_string(pair_string: str):
    [range_start_str, range_end_str] = pair_string.split('-')
    range_start, range_end = int(range_start_str), int(range_end_str)
    return (range_start, range_end)


total_p1 = 0
for pair in pairs:
    [range_1, range_2] = pair.split(',')
    r1_start, r1_end = get_range_ints_from_string(range_1)
    r2_start, r2_end = get_range_ints_from_string(range_2)
    if r2_start >= r1_start and r2_end <= r1_end:
        total_p1 += 1
        continue
    if r1_start >= r2_start and r1_end <= r2_end:
        total_p1 += 1


print(total_p1)

total_p2 = 0
for pair in pairs:
    [range_1, range_2] = pair.split(',')
    r1_start, r1_end = get_range_ints_from_string(range_1)
    r2_start, r2_end = get_range_ints_from_string(range_2)
    if r1_end >= r2_start and r2_end >= r1_start:
        total_p2 += 1
        continue
    if r2_end >= r1_start and r1_end >= r2_start:
        total_p2 += 1

print(total_p2)
