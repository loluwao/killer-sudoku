import pygame

from Board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (146, 129, 156)
BLUE = (7, 0, 128)
YELLOW = (255, 249, 168)
GREY = (105, 105, 105)

pygame.init()
pygame.display.set_caption("KILLER SUDOKU!")
b = Board()
f = pygame.font.SysFont("Arial", 30)
ff = pygame.font.SysFont("Arial", 12)
win = pygame.display.set_mode((720, 720))

possible_numers = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_BACKSPACE: 0
}
def draw_game():
    #pygame.time.delay(100)

    global num
    win.fill((255, 255, 255))

    # color current cell
    x = 135 + 50 * b.current_cell[0]
    y = 115 + 50 * b.current_cell[1]
    pygame.draw.rect(win, YELLOW if b.notes_mode else PURPLE, ((x, y), (50, 50)))

    # draw lines
    x, y = 135, 115
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(win, BLACK, (x, 115), (x, 565), thickness)
        pygame.draw.line(win, BLACK, (135, y), (585, y), thickness)
        x += 50
        y += 50

    # draw number buttons
    x = 135
    for i in range(1, 10):
        num = f.render(str(i), True, BLACK)
        pygame.draw.rect(win, BLACK, ((x, 600), (50, 50)), 1)
        win.blit(num, (x + 17, 607))
        x += 50

    # draw numbers on board
    x, y = 152, 122
    #num
    for i in range(9):
        for j in range(9):
            # number is given
            if b.starting_board[i][j] != 0:
                num = f.render(str(b.user_board[i][j].value), True, BLACK)
                win.blit(num, (x, y))
            elif b.starting_board[i][j] == 0: # number is not given
                if b.user_board[i][j].user_value != 0: # user has entered something
                    num = f.render(str(b.user_board[i][j].user_value), True, BLUE)
                    win.blit(num, (x, y))

            x += 50
        x = 152
        y += 50

    # draw notes
    x, y = 150, 120
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        for j in range(9):
            # every cell that doesn't already have a number entry
            if not b.user_board[i][j].given and b.user_board[i][j].user_value == 0:
                #print("{}, {}".format(j, i))
                for val in l:
                    # if note for # val is switched on/True
                    if b.user_board[i][j].notes[val]:
                        x = 145 + 50 * j + ((val - 1) % 3) * 12
                        y = 122 + 50 * i + ((val - 1) // 3) * 12
                        # display the note
                        num = ff.render(str(val), True, GREY)
                        win.blit(num, (x, y))


    # MODIFY LATER
    if b.game_over():
        pygame.draw.rect(win, WHITE, ((360, 360), (400, 200)))


    pygame.display.update()
    # pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY, 40, 40))

# returns the board coordinates of where the user clicked
def find_position(pos):
    x, y = pos[0], pos[1]
    if x <= 585 and x >= 135 and y >= 115:
        return ((x - 135) // 50, (y - 115) // 50)

b.print_board()

run = True
x, y = 0, 0
selected = ()
print(b.user_board[0][0].value)
while run:
    pygame.time.delay(100)
    #draw_game()
    #b.play_game()
    if not b.game_over():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # moving/arrow key events
                if event.key == pygame.K_RIGHT:
                    if x < 8: x += 1
                elif event.key == pygame.K_LEFT:
                    if x > 0: x -= 1
                elif event.key == pygame.K_UP:
                    if y > 0: y -= 1
                elif event.key == pygame.K_DOWN:
                    if y < 8: y += 1
                # number key events
                elif event.key in possible_numers:
                    if not b.notes_mode:
                        b.set_entry(possible_numers.get(event.key))
                        b.set_most_recent(y, x)
                        b.update_surrounding_notes()
                        #print(b.most_recent)
                    else:
                        if event.key == pygame.K_BACKSPACE:
                            b.reset_notes()
                        else:
                            b.change_cell_notes(possible_numers.get(event.key))
                # notes mode
                elif event.key == pygame.K_SPACE:
                    if not b.notes_mode: print("notes mode")
                    b.notes_mode = not b.notes_mode

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # clicked a cell on the board
                if pos[1] <= 565:
                    selected = find_position(pos)
                    if selected is not None:
                        x = selected[0]
                        y = selected[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
    b.set_current_cell(y, x)

    draw_game()



    # keys = pygame.key.get_pressed()

# draw_game()

pygame.quit()
