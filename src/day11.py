from math import floor, prod
import operator
import re
from typing import Callable

test_input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

with open('src/inputs/day11_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
puzzle_input = actual_input

ops = {
    "+": operator.add,
    "*": operator.mul
}


def create_monkeys_ref_from_input(input_str: str) -> dict:
    monkeys_ref = {}
    blocks = input_str.split('\n\n')
    for i, block in enumerate(blocks):
        start_items_str = re.search('Starting items: (.+)\n', block).group(1)
        start_items = [int(item) for item in start_items_str.split(', ')]
        operation_str = re.search('Operation: new = old (.+)\n', block).group(1)
        [op_str, op_var] = operation_str.split(' ')
        if op_var != 'old':
            op_var = int(op_var)
        test_value = int(re.search(r'divisible by (\d+)\n', block).group(1))
        true_dest = int(re.search(r'If true: throw to monkey (\d+)\n', block).group(1))
        false_dest = int(re.search(r'If false: throw to monkey (\d+)', block).group(1))
        monkeys_ref[i] = {"start_items": start_items,
                          "operator": ops[op_str],
                          "op_var": op_var,
                          "test_value": test_value,
                          "true_dest": true_dest,
                          "false_dest": false_dest,
                          "inspections": 0}
    return monkeys_ref


def process_rounds(monkeys_obj: dict, rounds: int, worry_reducer: Callable) -> int:
    for _ in range(0, rounds):
        for monkey in monkeys_obj.values():
            for item in monkey['start_items']:
                op_var = monkey['op_var']
                if op_var == 'old':
                    op_var = item
                worry_level = worry_reducer(monkey['operator'](item, op_var))
                if worry_level % monkey["test_value"] == 0:
                    monkeys_obj[monkey['true_dest']]['start_items'].append(worry_level)
                else:
                    monkeys_obj[monkey['false_dest']]['start_items'].append(worry_level)
                monkey['inspections'] += 1
            monkey['start_items'] = []
    inspections = [monkey['inspections'] for monkey in monkeys_obj.values()]
    monkey_business = prod(sorted(inspections, reverse=True)[0:2])
    return monkey_business


def worry_reducer_p1(worry_level: int, worry_variable: int = 3) -> int:
    return floor(worry_level / worry_variable)


monkeys_ref_p1 = create_monkeys_ref_from_input(puzzle_input)
monkey_business_p1 = process_rounds(monkeys_ref_p1, 20, worry_reducer_p1)
print('part 1:', monkey_business_p1)

# Part2
monkeys_ref_p2 = create_monkeys_ref_from_input(puzzle_input)
product_of_test_values = prod([monkey['test_value'] for monkey in monkeys_ref_p2.values()])


def worry_reducer_p2(worry_level: int, worry_variable: int = product_of_test_values) -> int:
    return worry_level % worry_variable


monkey_business_p2 = process_rounds(monkeys_ref_p2, 10000, worry_reducer_p2)
print('part 2:', monkey_business_p2)
