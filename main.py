import pygame

pygame.init()
win = pygame.display.set_mode((720, 720))
pygame.display.set_caption("KILLER SUDOKU!")

run = True


def draw_game():
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 255), (40, 40, 20, 20))
    #pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY, 40, 40))
    pygame.display.update()


while run:
    pygame.time.delay(100)
    draw_game()


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

keys = pygame.key.get_pressed()


draw_game()

pygame.quit()
