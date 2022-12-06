test_input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
with open('src/inputs/day6_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
buffer = actual_input

packet_marker_length = 4
for i in range(packet_marker_length, len(buffer)):
    block = buffer[i-packet_marker_length:i]
    block_set = set(block)
    if len(block_set) == packet_marker_length:
        print('packet marker', i)
        break

message_marker_length = 14
for i in range(message_marker_length, len(buffer)):
    block = buffer[i-message_marker_length:i]
    block_set = set(block)
    if len(block_set) == message_marker_length:
        print('message marker', i)
        break
