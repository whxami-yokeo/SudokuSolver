import tkinter as tk
from tkinter import messagebox


DIGITS = set(range(1, 10))


def candidates(board, row, col):
    """Return the numbers allowed in an empty cell."""
    used = set(board[row])
    used.update(board[r][col] for r in range(9))

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    used.update(
        board[r][c]
        for r in range(box_row, box_row + 3)
        for c in range(box_col, box_col + 3)
    )

    return DIGITS - used


def clues_are_valid(board):
    """Check whether the given numbers conflict with each other."""
    for row in range(9):
        for col in range(9):
            value = board[row][col]

            if value == 0:
                continue

            # Temporarily remove this number so it does not
            # conflict with itself during the check.
            board[row][col] = 0
            valid = value in candidates(board, row, col)
            board[row][col] = value

            if not valid:
                return False

    return True


def solve_board(board):
    """Solve in place using backtracking. Return True on success."""
    best_cell = None
    best_options = None

    # Choose the empty cell with the fewest possible numbers.
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                continue

            options = candidates(board, row, col)

            if not options:
                return False

            if best_options is None or len(options) < len(best_options):
                best_cell = (row, col)
                best_options = options

    # No empty cells remain.
    if best_cell is None:
        return True

    row, col = best_cell

    for number in sorted(best_options):
        board[row][col] = number

        if solve_board(board):
            return True

    board[row][col] = 0
    return False


class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.resizable(False, False)

        self.cells = [[None for _ in range(9)] for _ in range(9)]

        tk.Label(
            root,
            text="Enter the given numbers, then click Solve.",
            font=("Arial", 12),
        ).pack(padx=16, pady=(16, 10))

        # A dark background forms the lines between cells and boxes.
        grid_frame = tk.Frame(root, bg="black", padx=3, pady=3)
        grid_frame.pack(padx=16)

        validation = (
            root.register(self.valid_input),
            "%P",
        )

        for box_row in range(3):
            for box_col in range(3):
                box = tk.Frame(grid_frame, bg="black")
                box.grid(
                    row=box_row,
                    column=box_col,
                    padx=2,
                    pady=2,
                )

                for inner_row in range(3):
                    for inner_col in range(3):
                        row = box_row * 3 + inner_row
                        col = box_col * 3 + inner_col

                        cell = tk.Entry(
                            box,
                            width=2,
                            font=("Arial", 24),
                            justify="center",
                            fg="black",
                            bg="white",
                            insertbackground="black",
                            selectforeground="black",
                            selectbackground="#cce5ff",
                            relief="flat",
                            borderwidth=0,
                            highlightthickness=0,
                            validate="key",
                            validatecommand=validation,
                        )
                        cell.grid(
                            row=inner_row,
                            column=inner_col,
                            padx=1,
                            pady=1,
                            ipady=4,
                        )

                        self.cells[row][col] = cell

        buttons = tk.Frame(root)
        buttons.pack(pady=12)

        tk.Button(
            buttons,
            text="Solve",
            font=("Arial", 12),
            width=12,
            command=self.solve,
        ).pack(side="left", padx=5)

        tk.Button(
            buttons,
            text="Clear",
            font=("Arial", 12),
            width=12,
            command=self.clear,
        ).pack(side="left", padx=5)

        self.status = tk.StringVar(value="Leave unknown cells empty.")
        tk.Label(
            root,
            textvariable=self.status,
            font=("Arial", 10),
        ).pack(pady=(0, 12))

        self.cells[0][0].focus_set()

    @staticmethod
    def valid_input(value):
        """Allow an empty cell or exactly one digit from 1 to 9."""
        return value == "" or (len(value) == 1 and value in "123456789")

    def read_board(self):
        return [
            [
                int(cell.get()) if cell.get() else 0
                for cell in row
            ]
            for row in self.cells
        ]

    def solve(self):
        board = self.read_board()

        if not clues_are_valid(board):
            self.status.set("Conflicting numbers.")
            messagebox.showerror(
                "Invalid Sudoku",
                "A number is repeated in a row, column, or 3×3 box.",
                parent=self.root,
            )
            return

        if not solve_board(board):
            self.status.set("No solution found.")
            messagebox.showerror(
                "No Solution",
                "This puzzle has no solution. Check the given numbers.",
                parent=self.root,
            )
            return

        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.delete(0, tk.END)
                cell.insert(0, str(board[row][col]))

        self.status.set("Solved!")

    def clear(self):
        for row in self.cells:
            for cell in row:
                cell.delete(0, tk.END)

        self.status.set("Leave unknown cells empty.")
        self.cells[0][0].focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
