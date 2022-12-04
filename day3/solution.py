import string
from collections import Counter

with open("input.txt") as file:
    input = file.read().splitlines()

rucksacks_compartments = [(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in input]

priority = 0

for first_compartment, second_compartment in rucksacks_compartments:
    for item in first_compartment:
        if item in second_compartment:
            priority += string.ascii_letters.find(item) + 1
            break

print(priority)  # part 1

priority = 0

chunked_rucksacks = []
for index in range(0, len(input) - 1, 3):
    chunked_rucksacks.append(input[index:index+3])

for rucksacks in chunked_rucksacks:
    counter = Counter()
    for rucksack in rucksacks:
        counter.update(set(rucksack))
    priority += string.ascii_letters.find(counter.most_common()[0][0]) + 1

print(priority)  # part 2
