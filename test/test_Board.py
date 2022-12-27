from unittest import TestCase
from Board import Board
from Cell import Cell

b = Board()
class TestBoard(TestCase):

    def setUp(self):
        #b.initialize()
        print("")
    def testInitialize(self):

        # check that grid has right number of cells
        self.assertEqual(len(b.solution), 9)
        self.assertEqual(len(b.solution[0]), 9)

        b.print_board()

    def testCanAddNumber(self):
        # check that a number can be added to an empty board
        self.assertTrue(b.can_add_cell(0, 0, 4))

        # with 4 in slot (0, 3), check that a 4 can't be added to the
        # same row, column, or 3x3 block
        #b.set_cell(0, 3, 4)
        b.solution[0][3] = 4
        self.assertFalse(b.can_add_cell(0, 1, 4))
        self.assertFalse(b.can_add_cell(3, 3, 4))
        self.assertFalse(b.can_add_cell(1, 4, 4))

        # check that method returns true when adding a valid number
        self.assertTrue(b.can_add_cell(4, 4, 4))
        self.assertTrue(b.can_add_cell(4, 4, 9))

    def test_find_solution(self):
        grid1 = [[0, 0, 1, 7, 6, 0, 0, 0, 0],
                 [0, 0, 0, 0, 8, 0, 2, 5, 0],
                 [8, 2, 0, 4, 0, 9, 0, 1, 0],
                 [0, 9, 0, 5, 1, 0, 0, 3, 0],
                 [2, 1, 0, 0, 3, 6, 7, 0, 0],
                 [0, 5, 0, 8, 0, 4, 0, 9, 0],
                 [9, 6, 0, 0, 0, 0, 0, 0, 8],
                 [1, 0, 5, 6, 7, 0, 4, 0, 0],
                 [0, 7, 4, 2, 9, 0, 5, 0, 1]]
        #b.find_solution(grid1)
        print(grid1)