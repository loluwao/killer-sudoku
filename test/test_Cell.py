from unittest import TestCase
from Cell import Cell

c = Cell(0, 0, 9, False)


class TestCell(TestCase):
    def test_add_note(self):
        # check that number of notes starts at 0
        self.assertEqual(len(c.notes), 0)

        # add note and check that it's been added
        c.add_note(3)
        self.assertEqual(c.notes[0], 3)

        # try adding already existing note to make sure it isn't added again
        c.add_note(3)
        self.assertEqual(len(c.notes), 1)

    def test_remove_note(self):
        # add 2 notes to cell
        c.add_note(3)
        c.add_note(5)
        self.assertEqual(len(c.notes), 2)

        # try to remove a nonexistent node and check that nothing happens
        c.remove_note(4)
        self.assertEqual(len(c.notes), 2)

        # remove existing node
        c.remove_note(3)
        self.assertEqual(len(c.notes), 1)
