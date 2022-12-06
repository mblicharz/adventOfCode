from copy import deepcopy
from dataclasses import dataclass
from typing import Any

import aocd


@dataclass
class Movement:
    amount: int
    from_stack: int
    to_stack: int


StackItem = Any


class Stack:
    _stack: list[StackItem]

    def __init__(self, stack: list[StackItem]) -> None:
        self._stack = stack

    def pop(self, amount: int) -> list[StackItem]:
        output = []
        for index in range(0, amount):
            if len(self._stack) == 0:
                continue
            output.append(self._stack.pop(0))
        return output

    def append(self, items: list[StackItem], reversed: bool) -> None:
        if reversed:
            for item in items:
                self._stack.insert(0, item)
        else:
            for item in items[::-1]:
                self._stack.insert(0, item)

    def __getitem__(self, n: int):
        return self._stack[n]


class Stacks:
    _stacks: list[Stack]

    def __init__(self, stacks: list[Stack]) -> None:
        self._stacks = stacks

    def move_between_stacks(self, movement: Movement, reversed: bool = True) -> None:
        self._stacks[movement.to_stack].append(
            self._stacks[movement.from_stack].pop(movement.amount), reversed=reversed
        )

    def get_peak_items(self) -> list[StackItem]:
        return [stack[0] for stack in self._stacks]

    def copy(self) -> "Stacks":
        return deepcopy(self)


stacks = Stacks(
    [
        Stack(["G", "P", "N", "R"]),
        Stack(["H", "V", "S", "C", "L", "B", "J", "T"]),
        Stack(["L", "N", "M", "B", "D", "T"]),
        Stack(["B", "S", "P", "V", "R"]),
        Stack(["H", "V", "M", "W", "S", "Q", "C", "G"]),
        Stack(["J", "B", "D", "C", "S", "Q", "W"]),
        Stack(["L", "Q", "F"]),
        Stack(["V", "F", "L", "D", "T", "H", "M", "W"]),
        Stack(["F", "J", "M", "V", "B", "P", "L"]),
    ]
)

moves_input: str = aocd.get_data(year=2022, day=5).split("\n\n")[1]

moves_input: list[str] = moves_input.splitlines()

crane_movements = []
for line in moves_input:
    data = line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
    crane_movements.append(
        Movement(
            amount=int(data[0]),
            from_stack=int(data[1]) - 1,
            to_stack=int(data[2]) - 1,
        )
    )

part_1_stacks = stacks.copy()
for movement in crane_movements:
    part_1_stacks.move_between_stacks(movement)

print("".join(part_1_stacks.get_peak_items()))  # part 1

part_2_stacks = stacks.copy()
for movement in crane_movements:
    part_2_stacks.move_between_stacks(movement, reversed=False)

print("".join(part_2_stacks.get_peak_items()))  # part 2
