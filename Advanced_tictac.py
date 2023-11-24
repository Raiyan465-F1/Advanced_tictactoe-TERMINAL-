class Tictactoe:
    def __init__(self) :
        self.board = [" " for x in range(9)]
        self.player1 = "X"
        self.player2 = "O"

    
         
    #printing board
    def print_board(self) -> None:
        temp = self.board
        print(
            f"""
            |{temp[0]}|{temp[1]}|{temp[2]}|
            -------
            |{temp[3]}|{temp[4]}|{temp[5]}|
            -------
            |{temp[6]}|{temp[7]}|{temp[8]}|"""
        )

    #Updating board according to players move
    def update_board(self, key: str, index: str) -> None:

        self.board[int(index)-1] = key

    def check_for_winner(self) -> bool:
        # setting self.board as b so that it's easier to write
        b = self.board
        position = [0, 0, 3, 1, 6, 2]
        i = 0

        #checking rows and column
        while i < len(position):
            pos = position[i]

            if all(b[x] for x in range(pos, pos+3)):
                return True
            elif all(b[x] for x in range(pos, pos+7, 3)):
                return True    
            i+=1
        
        #chekcing diagonals
        

