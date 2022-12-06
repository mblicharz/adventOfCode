import aocd


def find_marker(datastream: str, marker_length: int) -> int:
    buffer = []
    for index, letter in enumerate(datastream):
        buffer.append(letter)
        if len(buffer) < marker_length:
            continue
        if len(set(buffer)) == marker_length:
            return index + 1
        buffer.pop(0)


input = aocd.get_data(year=2022, day=6)

print(find_marker(input, 4))  # part 1
print(find_marker(input, 14))  # part 2
