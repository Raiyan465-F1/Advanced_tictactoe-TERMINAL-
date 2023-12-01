
class Tictactoe:
    def __init__(self) :
        self.board = [x+1 for x in range(9)]
        self.key = None
        self.WinnerName = None
        self.resetlist = [self.board[:], self.key, self.WinnerName]
         
    def display_board(self) -> None:
        '''Prints the updated board '''
        temp = self.board
        print(
            f"""
            |{temp[0]}|{temp[1]}|{temp[2]}|
            -------
            |{temp[3]}|{temp[4]}|{temp[5]}|
            -------
            |{temp[6]}|{temp[7]}|{temp[8]}|"""
        )

    def update_board(self, key: str, index: str) -> None:
        '''Updates the board:
        first arguemnet takes what move(X or O)
        second arguemnt takes players position on the box (1-9)'''

        self.key = key
        self.board[int(index)-1] = key

    def ReturnWinnerName(self, name):
        self.WinnerName = name
        return True
        
        
    def check_for_winner(self) -> bool:
        '''Checks if there is a winner and returns True or False'''

        b = self.board #setting self.board as b so it's easier to write

        position1 = [0, 3, 6]
        position2 = [0, 1, 2]
        i = 0

        #checking rows and column
        while i < len(position1):
            pos1 = position1[i]
            pos2 = position2[i]

            if all([b[x] == self.key for x in range(pos1, pos1+3) if self.ReturnWinnerName(b[x])]):
                return (True, self.WinnerName)
            elif all([b[x] == self.key for x in range(pos2, pos2+7, 3) if self.ReturnWinnerName(b[x])]):
                return (True, self.WinnerName)
            i+=1

        
        #chekcing diagonals
        if all([b[x] == self.key for x in [0,4,8] if self.ReturnWinnerName(b[x])]):
            return (True, self.WinnerName)
        elif all([b[x] == self.key for x in [2,4,6] if self.ReturnWinnerName(b[x])]):
            return (True, self.WinnerName)
        else:
            return (False, False)
            
    
    def get_input(self) -> str:
        '''Takes and checks the input of a playher and returns it as a sttring'''
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

    #checking draw
    def check_draw(self) -> bool:
        '''Checks if it's a draw'''
        return all([not str(x).isnumeric() for x in self.board])
    
    def ResetOBJ(self):
        self.board, self.key, self.WinnerName = self.resetlist
        
            
            

