import asyncio

import pygame
import consts
import game_field
import time
import soldier
import random

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_welcome(welcome):
    if welcome:
        draw_message(consts.WELCOME_MESSAGE, consts.WELCOME_FONT_SIZE,
                 consts.WELCOME_COLOR, consts.WELCOME_LOCATION)

def draw_flag():
    img = pygame.image.load("flag.png").convert_alpha()
    img = pygame.transform.scale(img, (consts.FLAG_COLS*consts.CELL_SIZE, consts.FLAG_ROWS*consts.CELL_SIZE))
    screen.blit(img, consts.FLAG_LOCATION)


def draw_grass(grass_location):
    img = pygame.image.load("grass.png").convert_alpha()
    img = pygame.transform.scale(img, consts.GRASS_SIZE)
    screen.blit(img, grass_location)


def draw_mines():
    for i in range(consts.BOARD_ROWS):
        j = 0
        while j < consts.BOARD_COLS:
            if game_field.field[i][j] == 1:
                draw_mine((j*consts.CELL_SIZE,i*consts.CELL_SIZE))
                j += 3
            else:
                j+=1

def draw_grid():
    for x in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)

def draw_mine(mine_location):
    img = pygame.image.load("mine.png").convert_alpha()
    img = pygame.transform.scale(img, (consts.MINE_COLS*consts.CELL_SIZE, consts.MINE_ROWS*consts.CELL_SIZE))
    screen.blit(img, mine_location)

def draw_soldier(soldier_loc, soldier_state):
    img = pygame.image.load(soldier_state).convert_alpha()
    img = pygame.transform.scale(img, (consts.SOLDIER_COLS*consts.CELL_SIZE, consts.SOLDIER_ROWS*consts.CELL_SIZE))
    screen.blit(img, (soldier_loc[1]*consts.CELL_SIZE, soldier_loc[0]*consts.CELL_SIZE))

def draw_minefield(game_state):
    screen.fill(consts.BLACK)
    draw_grid()
    draw_mines()
    draw_soldier(game_state["soldier_location"], game_state["soldier_mode"])

    pygame.display.flip()

def draw_field(game_state):
    screen.fill(consts.GREEN)

    for grass in game_field.grass_location_list:
        draw_grass(grass)

    draw_flag()

    draw_soldier(game_state["soldier_location"], game_state["soldier_mode"])

    draw_welcome(game_state["welcome"])

    if game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()


