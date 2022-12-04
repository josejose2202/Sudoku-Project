import pygame
import sys
import math, random
from constants import *

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells= 30):
        self.row_length = row_length
        self.remove_cells = removed_cells
        self.board = []
        self.box_length = math.sqrt(row_length)
    def get_board(self):
        return [[0 for i in range(self.row_length)] for j in range(9)]

    def print_board(self):
        self.board = self.get_board()
        for row in self.board:  # row: ["-", "-", "-"]
            for col in row:
                print(col, end=" ")
            print()
    
    def valid_in_row(self, row, num):
        pass
    
    def valid_in_col(self, col, num):
        pass
    
    def valid_in_box(self, row, col, num):
        pass
    
    def is_valid(self, row, col, num):
        pass
    
    def fill_box(self, row_start, col_start):
        pass
    
    def fill_diagonal(self):
        pass
    
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
        pass

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

def game_start_screen(screen):
    start_title_font = pygame.font.Font(None, 85)
    game_mode_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 55)

    screen.fill(BG_COLOR)

    title = start_title_font.render("Welcome to Sudoku", 0, (66, 66, 66))
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//2 - 200))
    screen.blit(title, title_rect)

    game_mode_text = game_mode_font.render("Select Game Mode:", 0, (66, 66, 66))
    game_mode_rect = game_mode_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(game_mode_text, game_mode_rect)

    easy_text = button_font.render("EASY", 0, (255, 255, 255))
    easy_text_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_text_surf.fill((66, 66, 66))
    easy_text_surf.blit(easy_text, (10, 10))
    easy_text_rect = easy_text_surf.get_rect(center=(100, HEIGHT//2 + 100))
    screen.blit(easy_text_surf, easy_text_rect)


    medium_text = button_font.render("MEDIUM", 0, (255, 255, 255))
    medium_text_surf = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_text_surf.fill((66, 66, 66))
    medium_text_surf.blit(medium_text, (10, 10))
    medium_text_rect = medium_text.get_rect(center=(300, HEIGHT//2 + 100))
    screen.blit(medium_text_surf, medium_text_rect)

    hard_text = button_font.render("HARD", 0, (255, 255, 255))
    hard_text_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_text_surf.fill((66, 66, 66))
    hard_text_surf.blit(hard_text, (10, 10))
    hard_text_rect = hard_text.get_rect(center=(500, HEIGHT//2 + 100))
    screen.blit(hard_text_surf, hard_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_text_rect.collidepoint(event.pos):
                    return
                elif medium_text_rect.collidepoint(event.pos):
                    return
                elif hard_text_rect.collidepoint(event.pos):
                    return
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_start_screen(screen)
