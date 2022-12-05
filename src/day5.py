import re
from typing import List

test_crates = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 '''

test_moves = '''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

actual_crates = '''[N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]
 1   2   3   4   5   6   7   8   9 '''

with open('src/inputs/day5_input.txt', 'r', encoding='utf-8') as text:
    actual_moves = text.read()

crates = actual_crates
moves = actual_moves


def create_stack_from_string(stack_string: str) -> List[str]:
    crate_lines = stack_string.splitlines()
    number_of_stacks = int(crate_lines.pop().strip().split(' ')[-1])
    stacks = [[] for i in range(number_of_stacks)]
    for i, line in enumerate(crate_lines):
        stack_width = 4
        split_line = [line[i:i+stack_width] for i in range(0, len(line), stack_width)]
        for j, stack_spot in enumerate(split_line):
            if stack_spot.strip():
                stacks[j].insert(0, stack_spot[1])
    return stacks


stack_p1 = create_stack_from_string(crates)
move_lines = moves.splitlines()
for move_line in move_lines:
    n_crates, start, destination = [int(move) for move in re.findall('[0-9]+', move_line)]
    crates_to_move = stack_p1[start - 1][-n_crates:]
    crates_to_move.reverse()
    del stack_p1[start - 1][-n_crates:]
    stack_p1[destination - 1].extend(crates_to_move)

top_crates_p1 = ''.join([stack[-1] for stack in stack_p1])
print(top_crates_p1)

stack_p2 = create_stack_from_string(crates)
for move_line in move_lines:
    n_crates, start, destination = [int(move) for move in re.findall('[0-9]+', move_line)]
    crates_to_move = stack_p2[start - 1][-n_crates:]
    del stack_p2[start - 1][-n_crates:]
    stack_p2[destination - 1].extend(crates_to_move)

top_crates_p2 = ''.join([stack[-1] for stack in stack_p2])
print(top_crates_p2)
