class TicTacToe():
    def __init__(self):
        self.board = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]
        self.status = True
        self.move = 0
        self.showBoard()

    def play(self):
        if self.move % 2 == 0:
            self.move += 1
            self.p1play()
        else:
            self.move += 1
            self.p2play()

    def p1play(self):
        print("1. Player(X)\n")

        try:
            row = int(input("Row:\n"))
        except ValueError:
            row = 0
        while row<1 or row>3:
            try:
                print("Row value should be 1, 2 or 3")
                row = int(input("Row:\n"))
            except:
                print("You have entered a string\n")

        try:
            column = int(input("Column:\n"))
        except ValueError:
            column = 0
        while column<1 or column>3:
            try:
                print("Column value should be 1, 2 or 3")
                column = int(input("Column:\n"))
            except:
                print("You have entered a string\n")
        
        if self.checkTheSquare(row, column) == False:
            self.p1play()
        else:
            self.board[row-1][column-1] = " X "
            self.showBoard()
            self.checkTheGame()

    def p2play(self):
        print("2. Player(O)\n")

        try:
            row = int(input("Row:\n"))
        except ValueError:
            row = 0
        while row<1 or row>3:
            try:
                print("Row value should be 1, 2 or 3")
                row = int(input("Row:\n"))
            except:
                print("You have entered a string\n")

        try:
            column = int(input("Column:\n"))
        except ValueError:
            column = 0
        while column<1 or column>3:
            try:
                print("Column value should be 1, 2 or 3")
                column = int(input("Column:\n"))
            except:
                print("You have entered a string\n")
        
        if self.checkTheSquare(row, column) == False:
            self.p2play()
        else:
            self.board[row-1][column-1] = " O "
            self.showBoard()
            self.checkTheGame()

    def checkTheSquare(self, row, column):
        if self.board[row-1][column-1] == " X " or self.board[row-1][column-1] == " O ":
            print(f"This square is full ({self.board[row-1][column-1]})")
            self.showBoard()
            return False
        else:
            return True

    def showBoard(self):
        row = 1
        print("   1   2   3")
        for i in self.board:
            print(f"{str(row)} ", end="")
            row += 1
            for j in i:
                print(j, end=" ")
            print("\n")

    def checkTheGame(self):
        if self.move % 2 == 0:
            winner = "2. player (O) has won the game!"
        else:
            winner = "1. player (X) has won the game!"
        
        if [self.board[0][0], self.board[0][1], self.board[0][2]] == [" X ", " X ", " X "] or [self.board[0][0], self.board[0][1], self.board[0][2]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[1][0], self.board[1][1], self.board[1][2]] == [" X ", " X ", " X "] or [self.board[1][0], self.board[1][1], self.board[1][2]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[2][0], self.board[2][1], self.board[2][2]] == [" X ", " X ", " X "] or [self.board[2][0], self.board[2][1], self.board[2][2]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[0][0], self.board[1][0], self.board[2][0]] == [" X ", " X ", " X "] or [self.board[0][0], self.board[1][0], self.board[2][0]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[0][1], self.board[1][1], self.board[2][1]] == [" X ", " X ", " X "] or [self.board[0][1], self.board[1][1], self.board[2][1]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[0][2], self.board[1][2], self.board[2][2]] == [" X ", " X ", " X "] or [self.board[0][2], self.board[1][2], self.board[2][2]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == [" X ", " X ", " X "] or [self.board[0][0], self.board[1][1], self.board[2][2]] == [" O ", " O ", " O "]:
            self.status = False
        if [self.board[0][2], self.board[1][1], self.board[2][0]] == [" X ", " X ", " X "] or [self.board[0][2], self.board[1][1], self.board[2][0]] == [" O ", " O ", " O "]:
            self.status = False
            
        if not self.status:
            print(winner)
        if self.move == 9 and self.status:
            print("Draw\n")
            self.status = False

ticTacToe = TicTacToe()

while ticTacToe.status:
    ticTacToe.play()

