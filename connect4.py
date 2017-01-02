import sys

class Connect4Game():

    def __init__(self):
        self.board = [['-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-']]
        self.playerSymbols = ['X','O']
        self.turn = 0
        self.winner = None
        self.numMoves = 0
        
    def makeMove(self, column):
        if self.winner != None:
            raise ValueError("Game is already over, player %d won" % (self.winner + 1))
        if column > 5 or column < 0 or not isinstance(column, int):
            raise ValueError('Invalid move')
        self.numMoves += 1
        openCol = False
        for row in list(reversed(self.board)):
            if row[column] == '-':
                openCol = True
                row[column] = self.playerSymbols[self.turn]
                row = self.board.index(row)
                break
            
        if not openCol:
            raise ValueError('Invalid move, not an open column')
        
        self.board[row][column] = self.playerSymbols[self.turn]
        gameOver = self.checkWin(row, column)
        if gameOver:
            self.winner = self.turn 
        elif self.numMoves == 36:
            self.winner = "DRAW"
        self.turn = int(not self.turn)
        print(self)
        

    def checkHorizontal(self, row, column):
        sym = self.board[row][column]
        if column > 2:                                                              #checking three to the left
            if self.board[row][column - 1] == sym and self.board[row][column - 2] == sym and self.board[row][column - 3] == sym:
                return True
        else:                                                                       #checking three to the right
            if self.board[row][column + 1] == sym and self.board[row][column + 2] == sym and self.board[row][column + 3] == sym:
                return True

        if column > 2 and column < 5:                                                                  #checking two left one right
            if self.board[row][column - 1] == sym and self.board[row][column - 2] == sym and self.board[row][column + 1] == sym:
                return True
        elif column < 4 and column > 0:
            if self.board[row][column + 1] == sym and self.board[row][column + 2] == sym and self.board[row][column - 1] == sym:
                return True
        
        return False
    
    def checkVertical(self, row, column):
        sym = self.board[row][column]
        if row < 3:                                 #check 3 below
            if self.board[row + 1][column] == sym and self.board[row + 2][column] == sym and self.board[row + 3][column] == sym:
                return True
        
        return False
        
    def checkDiagnols(self, row, column):
        if self.checkLeftDiagnol(row, column):
            return True
        if self.checkRightDiagnol(row, column):
            return True
        return False
    
    def checkRightDiagnol(self, row, column):
        sym = self.board[row][column]
        if row > 2 and column < 3:                                             #up left three
            if self.board[row - 1][column + 1] == sym and self.board[row - 2][column + 2] == sym and self.board[row - 3][column + 3] == sym:
                return True
        if row > 1 and row < 5 and column > 0 and column < 4:                                             #up left 2
            if self.board[row + 1][column - 1] == sym and self.board[row - 1][column + 1] == sym and self.board[row - 2][column + 2] == sym:
                return True

        if row < 3 and column > 2:
            if self.board[row + 1][column - 1] == sym and self.board[row + 2][column - 2] == sym and self.board[row + 3][column - 3] == sym:
                return True

        if row < 4 and row > 0 and column < 5 and column > 1:
            if self.board[row - 1][column + 1] == sym and self.board[row + 1][column - 1] == sym and self.board[row + 2][column - 2] == sym:
                return True
            
        return False
        
    def checkLeftDiagnol(self, row, column):
        sym = self.board[row][column]

        if row > 2 and column > 2:                                             #up left three
            if self.board[row - 1][column - 1] == sym and self.board[row - 2][column - 2] == sym and self.board[row - 3][column - 3] == sym:
                return True
        if row > 1 and row < 5 and column < 5 and  column > 1:                                             #up left 2
            if self.board[row + 1][column + 1] == sym and self.board[row - 1][column - 1] == sym and self.board[row - 2][column - 2] == sym:
                return True

        if row < 3 and column < 3:
            if self.board[row + 1][column + 1] == sym and self.board[row + 2][column + 2] == sym and self.board[row + 3][column + 3] == sym:
                return True

        if row < 4 and row > 0 and column < 4 and column > 0:
            if self.board[row - 1][column - 1] == sym and self.board[row + 1][column + 1] == sym and self.board[row + 2][column + 2] == sym:
                return True
            
        return False
        return False
    
    def checkWin(self, row, column):
        if self.checkHorizontal(row, column):
            return True
        if self.checkVertical(row, column):
            return True
        if self.checkDiagnols(row, column):
            return True
        return False
    
    def __str__(self):
        boardStr = "\n"
        for row in self.board:
            for x in row:
                boardStr += x
                boardStr += ' '
            boardStr += '\n'
        return boardStr
    
if __name__ == "__main__":
    newGame = Connect4Game()
    print(newGame)
    while newGame.winner == None:
            move = int(input('\n>> '))
            newGame.makeMove(move)

        
    print(newGame)
##    for x in range(7):
##        if x % 2 == 0:
##            newGame.makeMove(int(x / 2),0)
##        else:
##            newGame.makeMove(int(x / 2),1)
            
    print(newGame)
    print("Winner: Player", newGame.winner)