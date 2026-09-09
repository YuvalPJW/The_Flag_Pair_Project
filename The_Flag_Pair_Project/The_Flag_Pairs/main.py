import pygame
import consts
import game_field
import screen
import soldier
import time

state = {
    "show_mines": False,
    "showed_mines": False,
    "welcome": True,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "soldier_location": consts.SOLDIER_START,
    "soldier_is_moving": False,
    "soldier_move": consts.SOLDIER_MOVE,
    "soldier_mode": consts.DAY_SOLDIER
}


def main():
    pygame.init()
    game_field.create_field()
    game_field.place_grass()
    game_field.mines_where()

    while state["is_window_open"]:

        handle_user_events()

        if state["soldier_is_moving"]:

            move_soldier()

            if soldier.hit_mine(state["soldier_location"]):
                state["state"] = consts.LOSE_STATE

            if soldier.hit_flag(state["soldier_location"]):
                state["state"] = consts.WIN_STATE

        if state["show_mines"]:
            state["soldier_mode"] = consts.NIGHT_SOLDIER
            screen.draw_minefield(state)
            pygame.time.wait(1000)
            state["show_mines"] = False

        else:
            state["soldier_mode"] = consts.DAY_SOLDIER

            screen.draw_field(state)


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not state["showed_mines"]:
                    state["show_mines"] = True
                    state["showed_mines"] = True

            elif event.key == pygame.K_UP:
                lst = list(state["soldier_move"])
                lst[0] = -1
                state["soldier_move"] = lst
                state["soldier_is_moving"] = True

            elif event.key == pygame.K_DOWN:
                lst = list(state["soldier_move"])
                lst[0] = 1
                state["soldier_move"] = lst
                state["soldier_is_moving"] = True

            elif event.key == pygame.K_LEFT:
                lst = list(state["soldier_move"])
                lst[1] = -1
                state["soldier_move"] = lst
                state["soldier_is_moving"] = True

            elif event.key == pygame.K_RIGHT:
                lst = list(state["soldier_move"])
                lst[1] = 1
                state["soldier_move"] = lst
                state["soldier_is_moving"] = True

            state["welcome"] = False


def move_soldier():
    lst = list(state["soldier_location"])
    lst[0] += state["soldier_move"][0]
    lst[1] += state["soldier_move"][1]
    if soldier.soldier_in_field(lst):
        state["soldier_location"] = lst
    state["soldier_move"] = consts.SOLDIER_MOVE
    state["soldier_is_moving"] = False


if __name__ == '__main__':
    main()
