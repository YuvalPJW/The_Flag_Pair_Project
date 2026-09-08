

import pygame
import consts
import game_field
import screen
import soldier

state = {
    "show_mines": False,
    "welcome": True,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}


def main():

    pygame.init()

    while state["is_window_open"]:

        handle_user_events()

        screen.draw_game(state)

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue
        #
        # if event.type == pygame.
        #
        # if event.type == pygame.MOUSEMOTION:
        #     rotate_arrow()
        #
        # elif event.type == pygame.MOUSEBUTTONDOWN and \
        #         not state["is_bubble_fired"] and \
        #         not state["bubbles_popping"]:
        #     fire_bubble()

