import copy
import random

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
                random.seed()

                random.shuffle(options)
                #print(options)
                for num in options:
                    if self.can_add_cell(self.solution, r, c, num):
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

    def restart(self):
        self.solution = []
        self.user_board = []
        self.starting_board = []
        # set board with 0's
        for i in range(9):  # row
            row = []
            for j in range(9):  # col
                row.append(0)
            self.solution.append(row)
        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
            self.user_board.append(row)

        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
            self.starting_board.append(row)

        self.initialize()
        # self.print_board()
        self.remove_nums()
        self.copy_solution()
        self.most_recent = ()
        # self.set_current_cell(0, 0)


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
    def can_add_cell(self, grid, row, column, number_to_add):
        # check row
        for cell in grid[row]:
            if cell == number_to_add:
                return False

        # check column
        for i in grid:
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
                if grid[r][c] == number_to_add:
                    return False

        # if all tests pass
        return True

    def empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return True

        return False
    def solve(self, current_grid):
        for i in range(0, 81):
            row = i // 9
            col = i % 9

            if current_grid[row][col] == 0:
                for num in range(1, 10):
                    if self.can_add_cell(current_grid, row, col, num):
                        current_grid[row][col] = num
                        for y in range(9):
                            for x in range(9):
                                if not self.empty_cell(current_grid):
                                    self.num_solutions += 1
                                    break
                                else:
                                    if self.solve(current_grid):
                                        return True

                break

                current_grid[row][col] = 0
        return False

    def num_empty(self, grid):
        count = 0
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    count += 1
        return count

    def get_avail_squares(self, grid):
        ls = []
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    ls.append((i, j))
        random.shuffle(ls)
        return ls

    # removes numbers that won't be visible on the board
    def remove_nums(self):
        # copy solution
        for i in range(9):
            for j in range(9):
                self.starting_board[i][j] = self.solution[i][j]

        squares_left = self.get_avail_squares(self.starting_board)
        count = len(squares_left)
        turns = 3
        c = 0
        while turns > 0 and count >= 17:
            print("turn " + str(turns) + ": starting with " + str(self.num_empty(self.starting_board)) + " empty cells")
            '''
            cell, row, col = 0, 0, 0
            while cell == 0:
                # pick random row and column
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                cell = self.solution[row][col]
            '''
            row, col = squares_left.pop()
            print(str(row) + ", " + str(col))
            count -= 1
            cell = self.starting_board[row][col]

            self.starting_board[row][col] = 0
            self.num_solutions = 0
            self.solve(copy.deepcopy(self.starting_board))
            c += 1
            if self.num_solutions != 1:
                #print("tried removing " + str(cell) + " didn't work")
                self.starting_board[row][col] = cell
                count += 1
                turns -= 1

        print("total rounds " + str(c))
        '''
        nums = random.randint(100, 175)
        for x in range(nums):  # CHANGE BACK
            cell, row, col = 0, 0, 0
            while cell == 0:
                # pick random row and column
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                cell = self.solution[row][col]

            # check if it's part of an unavoidable set
            self.starting_board[row][col] = 0
            self.num_solutions = 0
            self.solve(self.starting_board)
            #print(self.num_solutions)

            if self.num_solutions != 1:
                self.starting_board[row][col] = self.solution[row][col]
                #x -= 1
                '''

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
