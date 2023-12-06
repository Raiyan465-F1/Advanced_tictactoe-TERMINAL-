from Advanced_tictac import Tictactoe
import time
def Playgame(prevwinner: str) -> str:
    '''Plays a tictactoe game where the first move is parameteter and returns the winners name(X or O)'''
    dict_player = {"X": "Player 1", "O": "Player 2"}
    finding_out_second = [x for x in dict_player if x != prevwinner]
    second_player = finding_out_second[0]

    tttoe = Tictactoe()
    while True:
        # PLAYER 1S MOVE
        tttoe.display_board("Child")

        print(f"{dict_player[second_player]}'s move: {second_player}")
        player1:str = tttoe.get_input()

        #Updating board to new move
        tttoe.update_board(second_player, player1)
        

        # Checking for winner or draw
        try:
            flag, winner = tttoe.check_for_winner()
        except TypeError:
            flag, winner = False, False
        if flag:
            tttoe.display_board("Child")
            print(f"{dict_player[winner]} wins childbox")
            return winner
        
        elif tttoe.check_draw():
            tttoe.display_board("Child")
            print("It's a draw")
            Delaytime()
            tttoe.ResetOBJ()
            continue
        prevwinner, second_player = second_player, prevwinner
            

def Delaytime():
    time.sleep(0.5)
    print(f"playing again in....")
    for i in range(3):
        time.sleep(0.5)
        print(i+1)
        
