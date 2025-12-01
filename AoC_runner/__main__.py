from concurrent.futures.process import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter
from typing import Literal

from AoC_runner.year2025.solvers.puzzle1 import Puzzle1Part1Solver, Puzzle1Part2Solver
from AoC_runner.solver_base import PuzzleSolver

ALL_SOLVERS: dict[str, list[type[PuzzleSolver]]] = {
    "2025": [Puzzle1Part1Solver, Puzzle1Part2Solver]
}


def input_file(year: str, day: int) -> Path:
    file = Path(f"input/{year}/{day}.txt")

    if not file.exists():
        raise RuntimeError(
            f"Puzzle input for year {year}, day {day} not found. Download from <https://adventofcode.com/{year}/day/{day}/input>, save to {file.absolute()}"
        )

    return file


def run_solver(
    args: tuple[str, type[PuzzleSolver]],
) -> tuple[int, Literal[1] | Literal[2], int, int]:
    year, solver_cls = args
    solver = solver_cls()

    p_input = input_file(year, solver.number).read_text().rstrip().split("\n")

    start_time = perf_counter()
    solution = solver.solve(p_input)
    runtime = perf_counter() - start_time

    return solver.number, solver.part, int(runtime * 1000), solution


def run_solvers_for_year(year: str) -> None:
    solvers = ALL_SOLVERS[year]

    with ProcessPoolExecutor() as e:
        results = list(e.map(run_solver, ((year, solver) for solver in solvers)))

    for result in sorted(results, key=lambda x: x[0] * 2 + x[1]):
        day, part, runtime, solution = result
        print(f"Day {day: >2}, part {part}, took {runtime}ms\tSolution: {solution}")


def main() -> None:
    for year in ALL_SOLVERS:
        print(f"Running solvers for year {year}")
        run_solvers_for_year(year)


if __name__ == "__main__":
    main()
