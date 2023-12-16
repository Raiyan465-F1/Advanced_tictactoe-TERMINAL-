from childTictactoe import Playgame
from Advanced_tictac import Tictactoe
import time

def main():
    greater_tttoe = Tictactoe() # the parent tictactoe has been called greater_tttoe
    player_input = None
    subwinner = None
    sub_board_first_play = {"X": "Player 1", "O": "Player 2"} #We are taking X as player 1 and O as player 2

    time.sleep(0.5)

    print("player1 is X and player2 is O")
    time.sleep(0.5)
    print("Player 1(x), choose one childbox: ")
    greater_tttoe.display_board("Parent")
    player_input = greater_tttoe.get_input() #took input of player 1 

    timdelay(f"sub-board {player_input}") #A time delayed text

    subwinner = Playgame("X") #winner of child tictactoe and the parameter takes the first move(player) of the game.
    greater_tttoe.update_board(subwinner, player_input)

    #UPTO HERE FIRST MOVE AND GAME INITIATION HAS BEEN DONE 

    while True: # a loop for rest of the moves
        time.sleep(1)
        greater_tttoe.display_board("Parent")
        time.sleep(0.5)
        print(f"{sub_board_first_play[subwinner]} won childbox, {sub_board_first_play[subwinner]} choose next childbox")

        time.sleep(0.25)
        player:str = greater_tttoe.get_input()
        timdelay(f'sub_board {player}:')
        subwinner = Playgame(subwinner)
        greater_tttoe.update_board(subwinner, player)

        if greater_tttoe.check_for_winner()[0]:
            time.sleep(0.3)
            print("Congratulation")
            time.sleep(0.25)
            print(f"{sub_board_first_play[subwinner]} wins the game")
            break
        elif greater_tttoe.check_draw():
            print("It's a draw")

def timdelay(text):
    print(f"Swtich to {text} in.....")
    for i in range(3, 0, -1):
        time.sleep(0.5)
        print(i)
    
main()
