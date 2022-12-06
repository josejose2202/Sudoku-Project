import pygame
import sys
import math, random
from constants import *

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


def game_start_screen(screen):
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
                elif medium_text_rect.collidepoint(event.pos):
                    display_board(screen)
                elif hard_text_rect.collidepoint(event.pos):
                    display_board(screen)
        pygame.display.update()

def display_board(screen):
    button_font = pygame.font.Font(None, 55)
    surface = pygame.display.set_mode((600, 600))
    surface.fill(BG_COLOR)
    pygame.display.flip()

    easy_text = button_font.render("Reset", 0, (255, 255, 255))
    easy_text_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_text_surf.fill((66, 66, 66))
    easy_text_surf.blit(easy_text, (10, 10))
    easy_text_rect = easy_text_surf.get_rect(center=(100, HEIGHT // 2 + 260))
    screen.blit(easy_text_surf, easy_text_rect)

    medium_text = button_font.render("Restart", 0, (255, 255, 255))
    medium_text_surf = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_text_surf.fill((66, 66, 66))
    medium_text_surf.blit(medium_text, (10, 10))
    medium_text_rect = medium_text.get_rect(center=(300, HEIGHT // 2 + 250))
    screen.blit(medium_text_surf, medium_text_rect)

    hard_text = button_font.render("Exit", 0, (255, 255, 255))
    hard_text_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_text_surf.fill((66, 66, 66))
    hard_text_surf.blit(hard_text, (10, 10))
    hard_text_rect = hard_text.get_rect(center=(500, HEIGHT // 2 + 250))
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


def outline_text(x, y, string, col=black, size=55):
    draw_text(x + 2, y - 2, string, col, size, screen)
    draw_text(x - 2, y - 2, string, col, size, screen)
    draw_text(x + 2, y + 2, string, col, size, screen)
    draw_text(x - 2, y + 2, string, col, size, screen)
    draw_text(x, y, string, white, size, screen)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_start_screen(screen)

    game_over = True
    winner = True

    # game is over
    while True:
        if game_over:
            pygame.display.update()
            pygame.time.delay(1000)
            draw_game_over(screen)
        pygame.display.update()
