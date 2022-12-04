import aocd

input = [
    sum([int(calories) for calories in item.splitlines()])
    for item in aocd.get_data(year=2022, day=1).split("\n\n")
]

print(max(input))  # part 1
print(sum(sorted(input, reverse=True)[:3]))  # part 2
