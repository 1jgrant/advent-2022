test_input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
with open('src/inputs/day6_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
buffer = actual_input


def find_marker(buffer: str, marker_length: int) -> int:
    for i in range(marker_length, len(buffer)):
        block_set = set(buffer[i-marker_length:i])
        if len(block_set) == marker_length:
            return i


print(find_marker(actual_input, 4))
print(find_marker(actual_input, 14))
