import pygame

import consts
import game_field
import screen
import main

def hit_mine(solider_location):
    soldier_left = solider_location[0]+3, solider_location[1]
    soldier_right = solider_location[0]+3, solider_location[1]+1
    if soldier_left in game_field.mine_location_list or soldier_right in game_field.mine_location_list:
        return True
    return False

def soldier_in_field(solider_location):
    if 0<= solider_location[1] and solider_location[1]+1 <= consts.BOARD_COLS and 0<= solider_location[0] and solider_location[0]+4 <= consts.BOARD_ROWS:
        return True
    return False

def hit_flag(solider_location):
    if game_field.field[solider_location[0]][solider_location[1]] == 2 and game_field.field[solider_location[0]][solider_location[1]+1] == 2:
        return True
    return False
