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
        self.starting_board = None
        self.num_solutions = 0

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
        self.starting_board = self.solution
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
    def set_cell(self, row, col, num):
        self.solution[row][col].set_value(num)

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
        nums = random.randint(50, 65)
        for x in range(nums):
            cell, row, col = 0, 0, 0
            while cell == 0:
                # pick random row and column
                row = random.randint(0, 9)
                col = random.randint(0, 9)

                cell = self.starting_board[row][col]

            self.starting_board[row][col] = 0

    def copy_solution(self):
        for r in range(9):
            for c in range(9):
                self.user_board[r][c] = Cell(c, r, self.solution, 0, self.starting_board[r][c] != 0)
