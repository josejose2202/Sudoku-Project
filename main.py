import pygame
import sys
import math, random

import constants
from constants import *

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells= 0):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(9)]
        self.box_length = int(math.sqrt(row_length))
    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:  # row: ["-", "-", "-"]
            for col in row:
                print(col, end=" ")
            print()

    def valid_in_row(self, row, num):
        z = True
        x = "gfgfg"
        for val in self.board[row]:
            if num == val:
                x = "invaild"
                z = False
                break
            elif num != val:
                x= "vaild"
        if x == "invaild":
            return z
        else:
            return z


    def valid_in_col(self, col, num):
        z = True
        x = "gfgfg"
        for val in range(self.row_length):
            if self.board[val][col] == num:
                x = "invaild"
                z = False
                break
            elif num != val:
                x= "vaild"
        if x == "invaild":
            return z
        else:
            return z


    def valid_in_box(self, row_start, col_start, num):
        z = True
        x = "gfgfg"
        count = True
        while count:
            if row_start == 0 or row_start == 3 or row_start == 6:
                count = False
            else:
                row_start -= 1
        count1 = True
        while count1:
            if col_start == 0 or col_start == 3 or col_start == 6:
                count1 = False
            else:
                col_start -= 1
        for val in range(row_start,row_start+3):
            for val1 in range(col_start,col_start+3):
                if self.board[val][val1] == num:
                    x = "invaild"
                    z = False
                    break
                elif num != val:
                    x= "vaild"
            if x == "invaild":
                break
        return z

    def is_valid(self, row, col, num):
        if self.valid_in_box(row,col,num) == True and self.valid_in_col(col,num) == True and self.valid_in_row(row,num) == True:
            return True
        else:
            return False
    def fill_box(self, row_start, col_start):
        num = random.randint(1, 9)
        for val in range(3):
            for val1 in range(3):
                while self.valid_in_box(row_start,col_start,num) == False:
                    num = random.randint(1,9)
                self.board[row_start+val][col_start+val1] = num

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        count = self.removed_cells
        while count != 0:
            col = random.randint(0, 8)
            row = random.randint(0, 8)
            if self.board[col][row] != 0:
                count -= 1
            self.board[col][row] = 0



def generate_sudoku(size = 9, removed = 30):
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        board = sudoku.get_board()
        sudoku.remove_cells()
        board = sudoku.get_board()
        sudoku.print_board()
        return board

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        self.value = value

    def draw(self):
        chip_font = pygame.font.Font(None, NUM_FONT)
        chip_1_surf = chip_font.render('1', 0, COLOR)
        chip_2_surf = chip_font.render('2', 0, COLOR)
        chip_3_surf = chip_font.render('3', 0, COLOR)
        chip_4_surf = chip_font.render('4', 0, COLOR)
        chip_5_surf = chip_font.render('5', 0, COLOR)
        chip_6_surf = chip_font.render('6', 0, COLOR)
        chip_7_surf = chip_font.render('7', 0, COLOR)
        chip_8_surf = chip_font.render('8', 0, COLOR)
        chip_9_surf = chip_font.render('9', 0, COLOR)
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.col *
                                                              SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE,
                                                              SQUARE_SIZE), 12)
            self.selected = False


        if self.value == '1':
            chip_1_rect = chip_1_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_1_surf, chip_1_rect)
        elif self.value == '2':
            chip_2_rect = chip_2_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_2_surf, chip_2_rect)
        elif self.value == '3':
            chip_3_rect = chip_3_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_3_surf, chip_3_rect)
        elif self.value == '4':
            chip_4_rect = chip_4_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_4_surf, chip_4_rect)
        elif self.value == '5':
            chip_5_rect = chip_5_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_5_surf, chip_5_rect)
        elif self.value == '6':
            chip_6_rect = chip_6_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_6_surf, chip_6_rect)
        elif self.value == '7':
            chip_7_rect = chip_7_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_7_surf, chip_7_rect)
        elif self.value == '8':
            chip_8_rect = chip_8_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_8_surf, chip_8_rect)
        elif self.value == '9':
            chip_9_rect = chip_9_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE *
                        self.row + SQUARE_SIZE // 2))
            self.screen.blit(chip_9_surf, chip_9_rect)


def display_board(screen):
    button_font = pygame.font.Font(None, 55)
    surface = pygame.display.set_mode((600, 700))
    surface.fill(BG_COLOR)
    pygame.display.flip()

    easy_text = button_font.render("Reset", 0, (255, 255, 255))
    easy_text_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_text_surf.fill((66, 66, 66))
    easy_text_surf.blit(easy_text, (10, 10))
    easy_text_rect = easy_text_surf.get_rect(center=(100, HEIGHT // 2 + 360))
    screen.blit(easy_text_surf, easy_text_rect)

    medium_text = button_font.render("Restart", 0, (255, 255, 255))
    medium_text_surf = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_text_surf.fill((66, 66, 66))
    medium_text_surf.blit(medium_text, (10, 10))
    medium_text_rect = medium_text.get_rect(center=(300, HEIGHT // 2 + 350))
    screen.blit(medium_text_surf, medium_text_rect)

    hard_text = button_font.render("Exit", 0, (255, 255, 255))
    hard_text_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_text_surf.fill((66, 66, 66))
    hard_text_surf.blit(hard_text, (10, 10))
    hard_text_rect = hard_text.get_rect(center=(500, HEIGHT // 2 + 350))
    screen.blit(hard_text_surf, hard_text_rect)

class Board:
    def __init__(self, rows, cols, width, height, screen, removed=30):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.board = generate_sudoku(9, removed)
        self.cells = [
            [Cell(self.board[i][j], i, j, SQUARE_SIZE) for j in range(cols)]
            for i in range(rows)
        ]

    def initialize_board(self):
        # 1st approach
        return [["0" for i in range(9)] for j in range(9)]

    def draw(self):
        # draw horizontal lines
        for i in range(1, 10):
            pygame.draw.line(

                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )

        # draw vertical lines
        for j in range(1, 10):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH
            )
        for i in range(3, 10,3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR2,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH2
            )

        # draw vertical lines
        for j in range(3, 10,3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR2,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH2
            )

        # draw cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw()
            pygame.display.update()


def sudoku_game(screen):
    start_title_font = pygame.font.Font(None, 85)
    game_mode_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 55)
    bg = pygame.image.load("bg.jpeg")

    screen.blit(bg, (0, 30))

    outline_text(WIDTH // 2, HEIGHT // 2 - 200, "Welcome to Sudoku")

    outline_text(WIDTH // 2, HEIGHT // 2, "Select Game Mode:")

    easy_text = button_font.render("EASY", 0, (255, 255, 255))
    easy_text_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_text_surf.fill((66, 66, 66))
    easy_text_surf.blit(easy_text, (10, 10))
    easy_text_rect = easy_text_surf.get_rect(center=(100, HEIGHT // 2 + 110))
    screen.blit(easy_text_surf, easy_text_rect)

    medium_text = button_font.render("MEDIUM", 0, (255, 255, 255))
    medium_text_surf = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_text_surf.fill((66, 66, 66))
    medium_text_surf.blit(medium_text, (10, 10))
    medium_text_rect = medium_text.get_rect(center=(300, HEIGHT // 2 + 100))
    screen.blit(medium_text_surf, medium_text_rect)

    hard_text = button_font.render("HARD", 0, (255, 255, 255))
    hard_text_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_text_surf.fill((66, 66, 66))
    hard_text_surf.blit(hard_text, (10, 10))
    hard_text_rect = hard_text.get_rect(center=(500, HEIGHT // 2 + 100))
    screen.blit(hard_text_surf, hard_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_text_rect.collidepoint(event.pos):
                    display_board(screen)
                    removed = 30
                    board = Board(BOARD_ROWS, BOARD_COLS, WIDTH, HEIGHT, screen, removed)
                    board.draw()
                elif medium_text_rect.collidepoint(event.pos):
                    display_board(screen)
                    removed = 40
                    board = Board(BOARD_ROWS, BOARD_COLS, WIDTH, HEIGHT, screen, removed)
                    board.draw()
                elif hard_text_rect.collidepoint(event.pos):
                    display_board(screen)
                    removed = 50
                    board = Board(BOARD_ROWS, BOARD_COLS, WIDTH, HEIGHT, screen, removed)
                    board.draw()
        pygame.display.update()



def draw_game_over(screen):
    button_font = pygame.font.Font(None, 55)
    game_over_font = pygame.font.Font(None, 75)
    bg = pygame.image.load("bg.jpeg")

    screen.blit(bg, (0, 30))

    if winner:
        text = 'Game Won!'
    else:
        text = "Game Over :("

    outline_text(WIDTH // 2, HEIGHT // 2 - 135, text)

    if winner:
        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        exit_text_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_text_surf.fill((66, 66, 66))
        exit_text_surf.blit(exit_text, (10, 10))
        exit_text_rect = exit_text_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))
        screen.blit(exit_text_surf, exit_text_rect)
    else:
        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        restart_text_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_text_surf.fill((66, 66, 66))
        restart_text_surf.blit(restart_text, (10, 10))
        restart_text_rect = restart_text_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))
        screen.blit(restart_text_surf, restart_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if winner:
                if exit_text_rect.collidepoint(event.pos):
                    exit()
            else:
                if restart_text_rect.collidepoint(event.pos):
                    pass
    pygame.display.update()


def draw_text(x, y, string, col, size, window):
    font = pygame.font.SysFont("Impact", size)
    text = font.render(string, True, col)
    textbox = text.get_rect()
    textbox.center = (x, y)
    window.blit(text, textbox)


def outline_text(x, y, string, col=(0, 0, 0), size=55):
    draw_text(x + 2, y - 2, string, col, size, screen)
    draw_text(x - 2, y - 2, string, col, size, screen)
    draw_text(x + 2, y + 2, string, col, size, screen)
    draw_text(x - 2, y + 2, string, col, size, screen)
    draw_text(x, y, string, (255, 255, 245), size, screen)


if __name__ == "__main__":
    winner = False
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT1))
    sudoku_game(screen)
