

import pygame
import consts
import game_field
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
        draw_message(consts.WELCOME_MESSAGE, consts.WELCOME_MESSAGE,
                 consts.WELCOME_MESSAGE, consts.WELCOME_MESSAGE)

def draw_flag():
    img = pygame.image.load("flag.png").convert_alpha()
    screen.blit(img, (consts.FLAG_LOCATION))

def draw_grass(grass_location):
    img = pygame.image.load("grass.png").convert_alpha()
    screen.blit(img, (grass_location))

def draw_field():
    for i in range(20):
        location = random.randint(30, 200), random.randint(30,200)
        draw_grass(location)

def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)

    game_field.draw_field()

    if game_state["show_mines"]:
        game_field.draw_mines()

    draw_welcome(game_state["welcome"])

    soldier.draw()

    draw_flag()

    if game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()
