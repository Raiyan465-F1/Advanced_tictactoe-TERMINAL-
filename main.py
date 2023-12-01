from childTictactoe import Playgame
from Advanced_tictac import Tictactoe
import random
import time

def main():
    greater_tttoe = Tictactoe()
    first_play = False
    player_input = None
    sub_board_first_play = {"X": "Player 1", "O": "Player 2"}
    time.sleep(0.5)

    print("player1 is X and player2 is O")
    time.sleep(0.5)
    subwinner = None
    while True:
        if not first_play:
            print("Player 1(x), choose one sub-table: ")
            greater_tttoe.display_board()
            player_input = greater_tttoe.get_input()

            timdelay(f"sub-board {player_input}")
            subwinner = Playgame("O")
            greater_tttoe.update_board(subwinner, player_input)
            first_play = True
        time.sleep(1)
        greater_tttoe.display_board()
        time.sleep(0.5)
        print(f"{sub_board_first_play[subwinner]} won subboard, {sub_board_first_play[subwinner]}'s sub table")

        player:str = greater_tttoe.get_input()
        timdelay(f'sub_board {player}:')
        subwinner = Playgame(subwinner)
        greater_tttoe.update_board(subwinner, player)

        if greater_tttoe.check_for_winner()[0]:
            print(f"{sub_board_first_play[subwinner]} wins")
            break
        elif greater_tttoe.check_draw():
            print("It's a draw")



def timdelay(text):
    print(f"Swtich to {text} in.....")
    for i in range(3):
        time.sleep(0.5)
        print(i)
    
main()
