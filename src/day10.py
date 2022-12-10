test_input_small = '''noop
addx 3
addx -5
noop'''

with open('src/inputs/day10_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
puzzle_input = actual_input

operations = puzzle_input.splitlines()

cycle = 0
X = 1
during_cycle_values = {}
for operation in operations:
    if operation == 'noop':
        cycle += 1
        during_cycle_values[cycle] = X
        continue
    for i in range(0, 2):
        cycle += 1
        during_cycle_values[cycle] = X
        if i == 1:
            value = int(operation.split(' ')[1])
            X += value

target_cycles = [20, 60, 100, 140, 180, 220]
total_strength = 0
for cycle in target_cycles:
    signal_strength = cycle * during_cycle_values[cycle]
    total_strength += signal_strength

print('part 1:', total_strength)

crt_string = ''
for i in range(0, 240):
    sprite_middle = during_cycle_values[i + 1]
    sprite_range = range(sprite_middle - 1, sprite_middle + 2)
    if i % 40 in sprite_range:
        crt_string += '#'
        continue
    crt_string += '.'

print('part 2:')
for i in range(0, 6):
    print(crt_string[i * 40: (i + 1) * 40])
