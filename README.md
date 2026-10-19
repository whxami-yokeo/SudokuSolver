# Sudoku Solver

A Python GUI application for solving standard 9×9 Sudoku puzzles. Enter the given numbers into the grid and click **Solve** to fill in the remaining cells.

[![License: Custom](https://img.shields.io/badge/License-Custom-blue.svg)](LICENSE.md)
[![Last commit](https://img.shields.io/github/last-commit/whxami-yokeo/SudokuSolver)](https://github.com/whxami-yokeo/SudokuSolver/commits/main)


## Features

- Editable 9×9 Sudoku grid with clearly separated 3×3 boxes.
- Black text for both user-entered and solved numbers.
- Input validation that accepts only a single digit from 1 to 9 per cell.
- Solve button beneath the grid.
- Clear button to reset the board.
- Error messages for conflicting clues and puzzles with no solution.
- Backtracking solver that prioritizes cells with the fewest possible values.

## Requirements

- Python 3
- Tkinter available in your Python installation

The application does not use any third-party Python packages.

## Getting Started

1. Save the application code as `sudoku_gui.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python sudoku_gui.py
   ```

## How to Use

1. Enter the puzzle’s given numbers into the corresponding cells.
2. Leave unknown cells empty.
3. Click **Solve**.
4. The application fills in the remaining cells if a solution exists.
5. Click **Clear** to empty the grid and enter another puzzle.

All numbers appear in black, and the cells remain editable after solving.

### Input Rules

- Each cell accepts one digit from `1` to `9`.
- Leave a cell empty to mark it as unknown.
- Use Backspace or Delete to remove a number.
- Zero, letters, and multiple digits are not accepted.

### Error Messages

- **Invalid Sudoku:** A given number conflicts with another number in its row, column, or 3×3 box.
- **No Solution:** The clues do not immediately conflict, but the puzzle cannot be completed.

If an error occurs, check the entered clues, correct them, and try again.

## How It Works

The application represents the puzzle as a two-dimensional list, using `0` for empty cells.

Before solving, it checks whether any given numbers conflict. It then uses recursive backtracking:

1. Find the empty cell with the fewest valid candidate numbers.
2. Try a candidate that does not already appear in its row, column, or 3×3 box.
3. Continue solving the remaining cells.
4. If a choice leads to a dead end, undo it and try another candidate.
5. Stop when the board is complete or all possibilities have been exhausted.

The displayed grid is updated only after a complete solution is found.

## Code Overview

| Component           | Purpose                                                   |
|---------------------|-----------------------------------------------------------|
| `candidates()`      | Finds the numbers allowed in an empty cell.               |
| `clues_are_valid()` | Checks the given numbers for conflicts.                   |
| `solve_board()`     | Solves the board using recursive backtracking.            |
| `SudokuApp`         | Creates the GUI and handles input, solving, and clearing. |

## Limitations

- Supports standard 9×9 Sudoku puzzles only.
- Returns the first solution found; it does not check whether the solution is unique.
- Does not visually distinguish original clues from solved numbers.
- Solves on the GUI thread, so the window may become temporarily unresponsive during a lengthy search.
- Does not include puzzle saving, loading, or image recognition.

## License

This project is provided under a custom Display and Educational Use License.

Viewing, noncommercial educational use, and private educational modifications
are permitted under its terms. Commercial use and redistribution of the full
application require prior written permission.

See [LICENSE.md](LICENSE.md) for the complete terms.