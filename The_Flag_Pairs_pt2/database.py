
import pandas as pd
import game_field

def save_game(game_state):

    frame = pd.DataFrame.from_dict(game_state, orient='index')
    frame = frame.transpose()
    frame.to_csv("game_state.csv", index=False)


def load_game():
    df = pd.read_csv('game_state.csv')
    print(df.to_string())
    return df
