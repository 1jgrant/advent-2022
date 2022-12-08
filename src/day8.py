from typing import List

test_input = '''30373
25512
65332
33549
35390'''

with open('src/inputs/day8_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
puzzle_input = actual_input

input_lines = [list(line) for line in puzzle_input.splitlines()]


visible = len(input_lines) * 4 - 4
for i in range(1, len(input_lines) - 1):
    for j in range(1, len(input_lines) - 1):
        line = input_lines[i]
        target = line[j]
        left = line[:j]
        right = line[j+1:]
        max_left,  max_right = max(left), max(right)
        if target > max_left or target > max_right:
            visible += 1
            continue
        vertical = [line[j] for line in input_lines]
        above = vertical[:i]
        below = vertical[i+1:]
        max_above, max_below = max(above), max(below)
        if target > max_above or target > max_below:
            visible += 1

print('part 1:', visible)


def visible_trees(trees: List[str], target_tree: str):
    for i, tree in enumerate(trees):
        if tree >= target_tree:
            return i + 1
    return len(trees)


max_total = 0
for i in range(0, len(input_lines) - 1):
    for j in range(0, len(input_lines) - 1):
        line = input_lines[i]
        target = line[j]
        left = line[:j]
        right = line[j+1:]
        vertical = [line[j] for line in input_lines]
        above = vertical[:i]
        below = vertical[i+1:]
        view_right = visible_trees(right, target)
        view_left = visible_trees(list(reversed(left)), target)
        view_below = visible_trees(below, target)
        view_above = visible_trees(list(reversed(above)), target)
        total = view_left * view_right * view_below * view_above
        if total > max_total:
            max_total = total

print('part 2:', max_total)
