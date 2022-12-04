test_input = '''A Y
B X
C Z'''

with open('src/inputs/day2_input.txt', 'r', encoding='utf-8') as text:
    actual = text.read()

part_1_map = {
    "X": {"beats": "C", "equals": "A", "score": 1},
    "Y": {"beats": "A", "equals": "B", "score": 2},
    "Z": {"beats": "B", "equals": "C", "score": 3},
}

input_lines = actual.split('\n')
rounds = [item.split(' ') for item in input_lines]

score_p1 = 0
for choices in rounds:
    [their_key, your_key] = choices
    your_move = part_1_map[your_key]
    score_p1 += your_move["score"]
    if their_key == your_move["equals"]:
        score_p1 += 3
    if their_key == your_move["beats"]:
        score_p1 += 6

print(score_p1)

part_2_map = {
    'X': 0,
    'Y': 3,
    'Z': 6,
    "A": {'X': 'C', 'Y': 'A', 'Z': 'B', "score": 1},
    "B": {'X': 'A', 'Y': 'B', 'Z': 'C', "score": 2},
    "C": {'X': 'B', 'Y': 'C', 'Z': 'A', "score": 3},
}

score_p2 = 0
for choices in rounds:
    [their_key, result] = choices
    item = part_2_map[their_key]
    score_p2 += part_2_map[result] + part_2_map[item[result]]["score"]

print(score_p2)
