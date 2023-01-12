import random
from random import shuffle

from Cell import Cell


class Board:
    def __init__(self, solution=[], user_board=[]):
        self.solution = solution
        if solution == []:
            # set board with 0's
            for i in range(9):  # row
                row = []
                for j in range(9):  # col
                    row.append(0)
                self.solution.append(row)
        self.user_board = user_board
        if user_board == []:
            for i in range(9):
                row = []
                for j in range(9):
                    row.append(0)
                self.user_board.append(row)
        self.starting_board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
            self.starting_board.append(row)

        self.num_solutions = 0
        self.current_cell = (0, 0)  # (x, y)
        self.initialize()
        self.remove_nums()
        self.copy_solution()
        self.notes_mode = False
        self.most_recent = ()

    # initializes a solution board for the game
    def initialize(self):
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(81):
            r = x // 9
            c = x % 9
            if self.solution[r][c] == 0:
                shuffle(options)
                for num in options:
                    if self.can_add_cell(r, c, num):
                        self.solution[r][c] = num
                        if self.is_grid_full():
                            return True
                        else:
                            if self.initialize():
                                return True
                self.solution[r][c] = 0
                break
        # self.starting_board = self.solution
        return False

    # determines if solution board has been filled with numbers
    def is_grid_full(self):
        for r in self.solution:
            for c in r:
                if c == 0: return False
        return True

    # prints board to console (testing purposes)
    def print_board(self):
        for r in range(9):
            for c in range(9):
                print("{} ".format(self.solution[r][c]), end='')
            print("\n")

    # sets the slot at the given row and column to the given number
    # def set_cell(self, num):
    # self.user_board[self.current_cell[1]][self.current_cell[0]].set_user_value(num)

    # checks if a number can be put in that row and column
    def can_add_cell(self, row, column, number_to_add):
        # check row
        for cell in self.solution[row]:
            if cell == number_to_add:
                return False

        # check column
        for i in self.solution:
            if i[column] == number_to_add:
                return False

        # check 3x3 box
        # find coordinates of 3x3 box
        x = column // 3
        y = row // 3
        x *= 3
        y *= 3

        for r in range(y, y + 3):
            for c in range(x, x + 3):
                if self.solution[r][c] == number_to_add:
                    return False

        # if all tests pass
        return True

    # removes numbers that won't be visible on the board
    def remove_nums(self):
        for i in range(9):
            for j in range(9):
                self.starting_board[i][j] = self.solution[i][j]
        nums = random.randint(70, 75)
        for x in range(nums):  # CHANGE BACK
            cell, row, col = 0, 0, 0
            while cell == 0:
                # pick random row and column
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                cell = self.solution[row][col]

            self.starting_board[row][col] = 0

    # transfers solution to the board the user will see
    def copy_solution(self):
        for r in range(9):
            for c in range(9):
                self.user_board[r][c] = Cell(c, r, self.solution[r][c], 0, self.starting_board[r][c] != 0)

    # sets the current highlighted cell to the given coordinates
    def set_current_cell(self, row, col):
        self.current_cell = (col, row)

    def change_cell_notes(self, num):
        self.user_board[self.current_cell[1]][self.current_cell[0]].switch_note(num)

    def reset_notes(self):
        for x in range(1, 10):
            self.user_board[self.current_cell[1]][self.current_cell[0]].notes[x] = False

    # sets the current cell to the given number if it wasn't already given
    def set_entry(self, num):
        if self.user_board[self.current_cell[1]][self.current_cell[0]].given:
            print("You can't enter a number here, it was already given to you!")
        else:
            self.user_board[self.current_cell[1]][self.current_cell[0]].set_user_value(num)

    # determines if game has been won yet
    def game_over(self):
        for i in range(9):
            for j in range(9):
                if not self.user_board[i][j].given:
                    if not self.cell_is_allowed(i, j):
                        return False
        return True

    # for the game over function, checks if the cell in a rowxcolumn can be there
    def cell_is_allowed(self, row, col):
        num = self.user_board[row][col].user_value

        # check row
        for i in range(8):
            if self.user_board[row][i].user_value == num and i != col:
                return False

        # check column
        for i in range(8):
            if self.user_board[i][col].user_value == num and i != row:
                return False

        # check 3x3 box
        # find coordinates of 3x3 box
        x = col // 3
        y = row // 3
        x *= 3
        y *= 3

        for i in range(y, y + 3):
            for j in range(x, x + 3):
                if self.user_board[i][j] == num and i != row and j != col:
                    return False

        return True


    def set_most_recent(self, row, col):
        self.most_recent = (col, row)

    def update_surrounding_notes(self):
        # most recent user-entered value
        row = self.most_recent[1]
        col = self.most_recent[0]
        val = self.user_board[row][col].user_value

        # modify row
        for cell in self.user_board[row]:
            cell.notes[val] = False

        # modify col
        for r in self.user_board:
            r[col].notes[val] = False

        # modify 3x3 box
        x = col // 3
        y = row // 3
        x *= 3
        y *= 3

        for r in range(y, y + 3):
            for c in range(x, x + 3):
                self.user_board[r][c].notes[val] = False
