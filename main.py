def Playgame():
    from Advanced_tictac import Tictactoe

    tttoe = Tictactoe()

    def PlayGame():
        while True:
            # PLAYER 1S MOVE
            tttoe.display_board()

            print("Player 1's move: X")
            player1:str = tttoe.get_input()

            #Updating board to new move
            tttoe.update_board("X", player1)
            tttoe.display_board()

            # Checking for winner or draw
            if tttoe.check_for_winner()[0]:
                print("Player1 wins")
                break
            elif tttoe.check_draw():
                print("It's a draw")
                break

            # PLAYER 2S MOVE
            print("Player 2's move: O")
            player2:str = tttoe.get_input()

            # Updating board to new move
            tttoe.update_board("O", player2)
            
            #checking for winner or draw
            if tttoe.check_for_winner()[0]:

                tttoe.display_board()
                print("Player2 wins")
                break
            elif tttoe.check_draw():
                print("It's a draw")
                break

    PlayGame()