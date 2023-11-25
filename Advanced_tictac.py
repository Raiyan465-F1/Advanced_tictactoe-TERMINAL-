
class Tictactoe:
    def __init__(self) :
        self.board = [x+1 for x in range(9)]
        self.player1 = "X"
        self.player2 = "O"
        self.key = None
    
         
    #printing board
    def display_board(self) -> None:
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

        self.key = key
        self.board[int(index)-1] = key

    def check_for_winner(self) -> bool:
        # setting self.board as b so that it's easier to write
        b = self.board
        position1 = [0, 3, 6]
        position2 = [0, 1, 2]
        i = 0

        #checking rows and column
        while i < len(position1):
            pos1 = position1[i]
            pos2 = position2[i]

            if all([b[x] == self.key for x in range(pos1, pos1+3)]):
                return True
            elif all([b[x] == self.key for x in range(pos2, pos2+7, 3)]):
                return True    
            i+=1
        
        #chekcing diagonals
        if all([b[x] == self.key for x in [0,4,8]]):
            return True
        elif all([b[x] == self.key for x in [2,4,6]]):
            return True
            
    #getting and validating input
    def get_input(self):
        while True:
            try:
                player = input()
                if not self.board[int(player)-1].is_integer():
                    raise TypeError
                return player
            except (ValueError, IndexError):
                print("Move should be between 1-9")
            except AttributeError:
                print("Invalid move")

            


