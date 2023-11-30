from main import Playgame
from Advanced_tictac import Tictactoe
import random
import time

def main():
    greater_tttoe = Tictactoe()
    greater_tttoe.display_board()
    print("Player 1 choose one sub-table ")
    player_input = greater_tttoe.get_input()

def timdelay(text):
    print(f"Swtich to {text} in.....")
    for i in range(3):
        time.sleep(0.5)
        print()
    