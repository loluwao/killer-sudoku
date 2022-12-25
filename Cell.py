class Cell:
    def __init__(self, x_pos, y_pos, value, user_value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value
        self.user_value = user_value
        self.correct = False
        self.notes = []

    # adds the given number to the notes of the cell
    def add_note(self, num):
        # only add if given number is not already a note
        if self.notes.count(num) == 0:
            self.notes.append(num)

    # if found in the cell's notes, removes the number from notes
    def remove_note(self, num):
        if self.notes.count(num) > 0:
            self.notes.remove(num)