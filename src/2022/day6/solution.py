import aocd


def find_marker(datastream: str, marker_length: int) -> int:
    for index in range(0, len(datastream)):
        if len(set(datastream[index : index + marker_length])) == marker_length:
            return index + marker_length


input = aocd.get_data(year=2022, day=6)

print(find_marker(input, 4))  # part 1
print(find_marker(input, 14))  # part 2
