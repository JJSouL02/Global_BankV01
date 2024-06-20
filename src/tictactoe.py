class TicTacToe:
    def __init__(self, account):
        """Initialize the game board and set the current player."""
        self.board = self.getBlankBoard()
        self.currentPlayer = 'X'
        self.nextPlayer = 'O'
        self.account = account  # Pass in the account object

    def getBlankBoard(self):
        """Create a new, blank tic-tac-toe board."""
        board = {}  # The board is represented as a Python dictionary.
        for space in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            board[space] = ' '  # All spaces start as blank.
        return board

    def getBoardStr(self):
        """Return a text-representation of the board."""
        b = self.board
        return f'''
  {b['1']}|{b['2']}|{b['3']} 1 2 3
  -+-+-
  {b['4']}|{b['5']}|{b['6']} 4 5 6
  -+-+-
  {b['7']}|{b['8']}|{b['9']} 7 8 9'''

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space number
        and the space is blank."""
        return space in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and self.board[space] == ' '

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        b, p = self.board, player
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.board[space] == ' ':
                return False
        return True

    def updateBoard(self, space, mark):
        """Sets the space on the board to mark."""
        self.board[space] = mark

    def switchPlayer(self):
        """Switch the current player to the next player."""
        self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer

    def main(self):
        """Starts a new game of tic-tac-toe."""
        print('Welcome to tic-tac-toe!')

        while True:
            option = input("Press 'e' to exit or any other key to start the game: ").lower()
            if option == 'e':
                print("Exiting game.")
                break

            self.board = self.getBlankBoard()
            self.currentPlayer = 'X'

            self.playGame()

        print('Thanks for playing!')

    def playGame(self):
        """Runs a single game of tic-tac-toe."""
        while True:
            print(self.getBoardStr())  # Display the board on the screen.

            # Human player's turn
            move = None
            while not self.isValidSpace(move):
                print(f'What is {self.currentPlayer}\'s move? (1-9)')
                move = input()

            self.updateBoard(move, self.currentPlayer)  # Make the move.

            # Check if the game is over:
            if self.isWinner(self.currentPlayer):  # First check for victory.
                print(self.getBoardStr())
                print(self.currentPlayer + ' has won the game!')
                break
            elif self.isBoardFull():  # Next check for a tie.
                print(self.getBoardStr())
                print('The game is a tie!')
                break

            self.switchPlayer()  # Swap turns.

if __name__ == '__main__':
    # Main code to start the game
    account = None  # Assuming `account` is obtained
    game = TicTacToe(account)
    game.main()