import tkinter as tk #GUI toolkit
from tkinter import messagebox #displaying message boxes

class SudokuSolver:
  # initialize main window (master) 9x9 board and cells for user input
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.board = [[0] * 9 for _ in range(9)]
        self.cells = [[None] * 9 for _ in range(9)]
        self.create_board()

    # function to create 9x9 board for user entry
    def create_board(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.master, width=3, font=('Arial', 18), justify='center')
                cell.grid(row=row, column=col, padx=5, pady=5)
                self.cells[row][col] = cell
        
        # solve button to solve sudoku board automatically
        solve_button = tk.Button(self.master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)
        
        # clear button to remove all entries and values from the board
        clear_button = tk.Button(self.master, text="Clear", command=self.clear_board)
        clear_button.grid(row=10, column=0, columnspan=9, pady=10)


    # function to solve sudoku board using solve() functoin and display appropriate message
    def solve_sudoku(self):
        self.get_board()
        if self.solve():
            self.update_board()
            messagebox.showinfo("Success", "Sudoku solved!")
        else:
            messagebox.showerror("Error", "No solution exists!")

    # function to read values from GUI and update board array 
    def get_board(self):
        for row in range(9):
            for col in range(9):
                value = self.cells[row][col].get()
                self.board[row][col] = int(value) if value.isdigit() else 0

    # function to write the solved values back to the GUI cells
    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.board[row][col]))


    # function to clear the board and reset the array
    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.board[row][col] = 0

    # function to check if a value(num) placed in a cell (pos) is valid based on the row and column
    def is_valid(self, num, pos):
        row, col = pos
        
        # checking row to verify that value is unique
        for i in range(9):
            if self.board[row][i] == num and col != i:
                return False

        # checking column to verify that value is unique
        for i in range(9):
            if self.board[i][col] == num and row != i:
                return False

        # checking box (3x3 grid) to see if value is unique
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    # function to find a solution for the sudoku board using backtracking
    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    # function to find empty cell in the board 
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
