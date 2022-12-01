with open("input.txt") as file:
    input = [sum([int(calories) for calories in item.splitlines()]) for item in file.read().split("\n\n")]

print(max(input))  # part 1
print(sum(sorted(input, reverse=True)[:3]))  # part 2
