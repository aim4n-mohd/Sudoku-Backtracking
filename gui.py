import pygame
import sys
import random
import copy

#import existing functions
from Sudoku import cell_check, check_board, solve

pygame.init()

#---SETTINGS---
WIDTH, HEIGHT = 540, 650
ROWS, COLS = 9, 9
CELL_SIZE = WIDTH//COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
RED = (255, 100, 100)
BLUE = (100, 100, 255)

FONT = pygame.font.SysFont("arial", 40)
SMALL_FONT = pygame.font.SysFont("arial", 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoker")

#---GAME STATE---
board = [[0 for _ in range(9)] for _ in range(9)]
""" same as doing
board = []
for _ in range(9):
    row = []
    for _ in range(9):
        row.append(0)
    board.append(row)
"""

original_board = None
selected = None

mode = "edit"  #edit, play, solved


#---DRAW---
def draw_grid():
    for i in range(10):
        thickness = 4 if i%3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i*CELL_SIZE), (WIDTH, i*CELL_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (i*CELL_SIZE, 0), (i*CELL_SIZE, WIDTH), thickness)

def draw_numbers():
    for r in range(9):
        for c in range(9):
            if board[r][c] !=0:
                text = FONT.render(str(board[r][c]), True, BLACK)
                screen.blit(text, (c*CELL_SIZE + 15, r*CELL_SIZE + 5))

def highlight_selected():
    if selected:
        r, c = selected
        pygame.draw.rect(screen, BLUE, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

def draw_buttons():
    pygame.draw.rect(screen, GRAY, (0, 550, WIDTH, 50))

    solve_text = SMALL_FONT.render("SOLVE", True, BLACK)
    reset_text = SMALL_FONT.render("RESET", True, BLACK)
    generate_text = SMALL_FONT.render("GENERATE", True, BLACK)

    screen.blit(generate_text, (20, 560))
    screen.blit(solve_text, (200, 560))
    screen.blit(reset_text, (350, 560))

#---INPUT---
def get_cell(pos):
    x, y = pos
    if y < WIDTH:
        return y//CELL_SIZE, x//CELL_SIZE
    return None

#---GENERATE---
def generate(board):
    # to be added
    pass

#---MAIN LOOP---
running = True

while running:
    screen.fill(WHITE)
    draw_numbers()
    draw_grid()
    highlight_selected()
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #grid click
            cell = get_cell(pos)
            if cell:
                selected = cell

            #SOLVE BUTTON
            if 200 < pos[0] < 300 and 550 < pos[1] < 600:
                if mode!="solved":
                    
                    solve(board, 0, 0)
                    mode = "solved"

            #RESET
            if 350 < pos[0] < 450 and 550 < pos [1] < 600:
                board = [[0]*9 for _ in range(9)]
                mode = "edit"

        #KEYBOARD
        if event.type == pygame.KEYDOWN and selected:
            r, c = selected

            if event.unicode.isdigit():
                num = int(event.unicode)

                if num == 0:
                    board[r][c] = 0
                else:
                    board[r][c] = num
                    if not cell_check(board, r, c):
                        pygame.draw.rect(screen, RED, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.display.update()
                        pygame.time.delay(200)

                        board[r][c] = 0

    pygame.display.update()

pygame.quit()
sys.exit()

            
