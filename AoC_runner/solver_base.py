from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Literal


class PuzzleSolver(ABC):
    @abstractmethod
    def solve(self, puzzle_input: Iterable[str]) -> int:
        """
        Solve the puzzle with the given input
        :param puzzle_input: The input to operate on
        :return: The solution (a number)
        """
        pass

    @property
    @abstractmethod
    def number(self) -> int:
        """
        :return: The puzzle number this solver solves (e.g. 1 for the solver of the first puzzle)
        """
        pass

    @property
    @abstractmethod
    def part(self) -> Literal[1] | Literal[2]:
        """
        :return: The puzzle part this solver solves (e.g. Part.One for the first part of a puzzle)
        """
        pass
