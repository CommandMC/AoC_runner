from collections.abc import Iterable
from typing import Literal

from AoC_runner.solver_base import PuzzleSolver


class Puzzle1Part1Solver(PuzzleSolver):
    _dial_position: int
    _zero_hits: int

    @property
    def number(self):
        return 1

    @property
    def part(self):
        return 1

    def solve(self, puzzle_input: Iterable[str]) -> int:
        self._dial_position = 50
        self._zero_hits = 0

        for line in puzzle_input:
            direction = line[0]
            amount = int(line[1:])
            assert direction == "R" or direction == "L"
            self.apply_rotation(direction, amount)

        return self._zero_hits

    def apply_rotation(
        self, direction: Literal["L"] | Literal["R"], amount: int
    ) -> None:
        change = -amount if direction == "L" else amount
        self._dial_position = (self._dial_position + change) % 100
        if self._dial_position == 0:
            self._zero_hits += 1


class Puzzle1Part2Solver(Puzzle1Part1Solver):
    @property
    def part(self):
        return 2

    def apply_rotation(
        self, direction: Literal["L"] | Literal["R"], amount: int
    ) -> None:
        change = -amount if direction == "L" else amount
        incorrect_zero_hits, new_dial_pos = divmod(self._dial_position + change, 100)
        true_zero_hits = (
            abs(incorrect_zero_hits)
            - (1 if self._dial_position == 0 and direction == "L" else 0)
            + (1 if new_dial_pos == 0 and direction == "L" else 0)
        )
        self._zero_hits += true_zero_hits
        self._dial_position = new_dial_pos
