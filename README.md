### Advent of Code solvers

#### Repository layout

- The runner (running all solvers) is in `AoC_runner/__main__.py`
- Solvers & tests for a specific year are in `AoC_runner/year<year>`
  - Solvers (solving individual puzzle parts) are in the `solvers/` subdirectory
  - Tests for solvers (usually just testing with the example inputs provided) are in the `tests/` subdirectory

#### Setup

The usual Python project setup (create venv)

Step-by-step:
1. Ensure `git` and `python` are available
2. Clone the repository (`git clone ...`) and `cd` into it
3. Create a venv (`python -m venv .venv`) and activate it (`. ./.venv/bin/activate`)
4. Optional, but highly recommended: Open the project in PyCharm to use the provided run configurations

#### Usage

To run all solvers, use the "Run solvers on real inputs" run configuration or run the module from the terminal (`python -m AoC_runner`). Place required puzzle inputs into the directories as instructed.

To run tests, use the "Test solver implementation" run configuration or run the `unittest` Python module (`python -m unittest`)


#### Adding new solvers

1. Create a new file `AoC_runner/year<year>/solvers/puzzle<num>.py` if required
2. Define a class (usually `Puzzle<num>Part<num>Solver`) inheriting from `AoC_runner.solver_base.PuzzleSolver`
3. Implement the required methods
4. If you want to write a test for the solver: Add a test in the `AoC_runner/year<year>/tests/` directory
    - You may want to use the example input provided on the site as a test
    - Usually this test defines an instance of the relevant solver (`self.solver`) in the `setUp` method
5. Add the solver class to `AoC_runner/__main__.py`'s `ALL_SOLVERS`, in the relevant year's array
