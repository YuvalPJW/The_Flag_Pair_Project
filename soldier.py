import pygame
from fontTools.misc.cython import returns

import consts
import game_field
import screen
import main

solider=[1]


def solider_right_feet(location):
    leg=location[0]+1
    return leg

"""the left side of soliders head"""
def solider_head(location):
    head=location[j]-3
    return head

def hit_mine(game_fielsfield.field, solider.location):
for square in range(len(game_fielsfield.field)):
     if solider.location[0]==1 or solider_right_feet(solider.location)==1:
         return True

def hit_flag (game_fiels.field, solider.location):
for square in range(len(game_field.field)):
    if solider[0]==2 and solider_right_feet(solider.location)==2 and  solider_head(solider.location)==2:
        return True

""""i=row
j=colum
tuple(i,j)"""

def solider_doesnt_go_out_of_field(game_fiels.field, solider.location):
 while solider_head(solider.location)>=0 and solider_right_feet(solider.location)

