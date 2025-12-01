import unittest

from AoC_runner.year2025.solvers.puzzle1 import Puzzle1Part1Solver, Puzzle1Part2Solver


EXAMPLE_INPUT = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.solver = Puzzle1Part1Solver()

    def test_example_input(self):
        self.assertEqual(
            self.solver.solve(EXAMPLE_INPUT),
            3,
        )


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.solver = Puzzle1Part2Solver()

    def test_example_input(self):
        self.assertEqual(self.solver.solve(EXAMPLE_INPUT), 6)

    def test_zero_wrap(self):
        p_input = ["L50", "L5"]
        self.assertEqual(self.solver.solve(p_input), 1)
