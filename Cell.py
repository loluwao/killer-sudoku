class Cell:
    def __init__(self, x_pos, y_pos, value, user_value, given):
        # coordinates
        self.x_pos = x_pos
        self.y_pos = y_pos
        # value: actually solution value. user_value: number the user has entered
        self.value = value
        self.user_value = user_value
        self.given = given
        self.correct = False

        self.notes = {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            9: False
        }

    # adds the given number to the notes of the cell
    def switch_note(self, num):
        if not self.given:
            self.notes[num] = not self.notes[num]

    def set_user_value(self, num):
        self.user_value = num