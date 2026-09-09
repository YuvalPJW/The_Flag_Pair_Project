import random
import consts

field = [[0 for _ in range(consts.BOARD_COLS)] for _ in range(consts.BOARD_ROWS)]
grass_location_list = []
mine_location_list = []

def create_field():
    count = 0
    while count < consts.MINES_COUNT:
        i = random.randint(0, consts.BOARD_ROWS - 1)
        j = random.randint(0, consts.BOARD_COLS - 1)
        if field[i][j] != 1:
            field[i][j] = 1
            count += 1

    for i in range(consts.flag_row, consts.BOARD_ROWS):
        for j in range(consts.flag_col, consts.BOARD_COLS):
            field[i][j] = 2

def place_grass():
    for i in range(20):
        location = random.randint(0, consts.WINDOW_WIDTH-consts.GRASS_SIZE[0]), random.randint(0,consts.WINDOW_HEIGHT-consts.GRASS_SIZE[0])
        grass_location_list.append(location)


def mines_where():
    row_idx = 0
    col_idx = 0
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS-2):
            if field[row][col] == 1:
                mine = (row_idx, col_idx)
                mine1 = (row_idx, col_idx+1)
                mine2 = (row_idx, col_idx+2)
                mine_location_list.append(mine)
                mine_location_list.append(mine1)
                mine_location_list.append(mine2)
            col_idx += 1
        col_idx = 0
        row_idx += 1

