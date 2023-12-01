from Advanced_tictac import Tictactoe
import time
def Playgame(prevwinner):
    dict_player = {"X": "Player 1", "O": "Player 2"}
    finding_out_second = [x for x in dict_player if x != prevwinner]
    second_player = finding_out_second[0]

    tttoe = Tictactoe()
    while True:
        # PLAYER 1S MOVE
        tttoe.display_board()

        print(f"{dict_player[prevwinner]}'s move: {prevwinner}")
        player1:str = tttoe.get_input()

        #Updating board to new move
        tttoe.update_board(prevwinner, player1)
        tttoe.display_board()

        # Checking for winner or draw
        try:
            flag, winner = tttoe.check_for_winner()
        except TypeError:
            flag, winner = False, False
        if flag:
            print(f"{dict_player[winner]} wins")
            return winner
        
        elif tttoe.check_draw():
            print("It's a draw")
            Delaytime()
            tttoe.ResetOBJ()
            continue
            

        # PLAYER 2S MOVE
        print(f"{dict_player[second_player]}'s move: {second_player}")
        player2:str = tttoe.get_input()

        # Updating board to new move
        tttoe.update_board(second_player, player2)
        
        #checking for winner or draw
        flag, winner = tttoe.check_for_winner()
        if flag:
            tttoe.display_board()

            print(f"{dict_player[winner]} wins")
            return winner
        

        elif tttoe.check_draw():
            print("It's a draw")
            Delaytime()
            tttoe.ResetOBJ()
            continue


def Delaytime():
    time.sleep(0.5)
    print(f"playing again in....")
    for i in range(3):
        time.sleep(0.5)
        print(i+1)
        
