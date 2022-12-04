test_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

with open('src/inputs/day1_input.txt', 'r', encoding='utf-8') as text:
    actual = text.read()

calories = actual.split('\n\n')
calorie_groups = [item.splitlines() for item in calories]
calorie_totals = [sum(int(x) for x in calorie_group) for calorie_group in calorie_groups]
largest = max(calorie_totals)
print(largest)

sorted_totals = sorted(calorie_totals, reverse=True)
sum_top_three = sum(sorted_totals[0:3])
print(sum_top_three)
