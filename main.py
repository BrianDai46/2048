from grid_functions import *
import pygame

pygame.init()

# initial set up
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 144
font = pygame.font.Font('freesansbold.ttf', 24)

# 2048 game color library
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
full = False
spawn_new = True
init_count = 0
direction = ''

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board(screen, font, colors)
    draw_pieces(board_values, screen, colors)
    if spawn_new or init_count < 2:
        board_values, full = new_pieces(board_values)
        spawn_new = False
        init_count += 1
    if direction != '':
        board_values = take_turn(direction, board_values)
        direction = ''
        spawn_new = True
    if full and is_game_over(board_values):
        draw_over(screen, font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                direction = 'UP'
            elif event.key == pygame.K_s:
                direction = 'DOWN'
            elif event.key == pygame.K_a:
                direction = 'LEFT'
            elif event.key == pygame.K_d:
                direction = 'RIGHT'

            if full and is_game_over(board_values):
                if event.key == pygame.K_RETURN:
                    board_values = [[0 for _ in range(4)] for _ in range(4)]
                    spawn_new = True
                    init_count = 0
                    direction = ''
                    full = False

    pygame.display.flip()
pygame.quit()