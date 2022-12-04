from dataclasses import dataclass

import aocd


class AssignmentsPair:
    first: "AssignmentRange"
    second: "AssignmentRange"

    @dataclass
    class AssignmentRange:
        min: int
        max: int

    def __init__(
        self,
        first_assignment: list[int],
        second_assignment: list[int],
    ) -> None:
        self.first = self.AssignmentRange(*first_assignment)
        self.second = self.AssignmentRange(*second_assignment)

    def is_repeated(self) -> bool:
        return (
            (self.first.min <= self.second.min) and (self.second.max <= self.first.max)
        ) or (
            (self.second.min <= self.first.min) and (self.first.max <= self.second.max)
        )

    def is_overlapped(self) -> bool:
        return (self.first.min <= self.second.min <= self.first.max) or (
            self.second.min <= self.first.min <= self.second.max
        )


input = aocd.get_data(year=2022, day=4).splitlines()

pairs = []
for line in input:
    pairs.append(
        AssignmentsPair(
            *[[int(x) for x in pair.split("-")] for pair in line.split(",")]
        )
    )

repeated_assignments = 0
overlapped_assignments = 0

for pair in pairs:
    if pair.is_repeated():
        repeated_assignments += 1
    if pair.is_overlapped():
        overlapped_assignments += 1

print(repeated_assignments)  # part 1
print(overlapped_assignments)  # part 2
