from typing import List

test_input_small = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

test_input_large = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

with open('src/inputs/day9_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
puzzle_input = actual_input


def move_right(coords: List[int]):
    coords[0] += 1


def move_left(coords: List[int]):
    coords[0] -= 1


def move_up(coords: List[int]):
    coords[1] += 1


def move_down(coords: List[int]):
    coords[1] -= 1


move_ref = {
    "R": move_right,
    "L": move_left,
    "U": move_up,
    "D": move_down
}


def move_lead_knot(lead_key: str, direction: str, coords: dict):
    move_ref[direction](coords[lead_key])


def move_trailing_knot(trailing_key: str, lead_key: str, coords: dict):
    x_diff = coords[lead_key][0] - coords[trailing_key][0]
    y_diff = coords[lead_key][1] - coords[trailing_key][1]
    if abs(x_diff) > 1 and abs(y_diff) > 1:
        coords[trailing_key][0] += int(x_diff / abs(x_diff))
        coords[trailing_key][1] += int(y_diff / abs(y_diff))
    elif abs(x_diff) > 1 and abs(y_diff) == 1:
        coords[trailing_key][0] += int(x_diff / abs(x_diff))
        coords[trailing_key][1] = coords[lead_key][1]
    elif abs(y_diff) > 1 and abs(x_diff) == 1:
        coords[trailing_key][0] = coords[lead_key][0]
        coords[trailing_key][1] += int(y_diff / abs(y_diff))
    elif abs(x_diff) > 1:
        coords[trailing_key][0] += int(x_diff / abs(x_diff))
    elif abs(y_diff) > 1:
        coords[trailing_key][1] += int(y_diff / abs(y_diff))


lines = puzzle_input.splitlines()
coords_p1 = {
    's': [0, 0],
    'H': [0, 0],
    'T': [0, 0],
}
tail_visits_p1 = set()
for line in lines:
    [direction, distance] = line.split(' ')
    for _ in range(int(distance)):
        move_lead_knot("H", direction, coords_p1)
        move_trailing_knot("T", "H", coords_p1)
        tail_visits_p1.add(f'{coords_p1["T"]}')

print('part 1:', len(tail_visits_p1))

coords_p2 = {
    's': [0, 0],
}
for i in range(0, 10):
    coords_p2[f'{i}'] = [0, 0]
tail_visits_p2 = set()
for line in lines:
    [direction, distance] = line.split(' ')
    for _ in range(int(distance)):
        move_lead_knot("0", direction, coords_p2)
        for i in range(1, 10):
            move_trailing_knot(f'{i}', f'{i - 1}', coords_p2)
            if i == 9:
                tail_visits_p2.add(f'{coords_p2["9"]}')

print('part 2:', len(tail_visits_p2))
