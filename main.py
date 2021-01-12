import random

US = 'O'
CO = 'X'
WINNING_SETS = set([frozenset([1,2,3]), 
                    frozenset([4,5,6]), 
                    frozenset([7,8,9]), 
                    frozenset([1,5,9]), 
                    frozenset([3,5,7])])

class TicTacToe:
  def __init__(self):
    self.board = [' ', ' ', ' ',
                  ' ', ' ', ' ',
                  ' ', ' ', ' ']
    self.markCount = 0
    self.userMoves = set()
    self.comMoves = set()
    self.result = ""

  def printBoardAtStart(self):
    board = """
    --- --- --- 
    {1}|{2}|{3} 
    --- --- --- 
    {4}|{5}|{6} 
    --- --- --- 
    {7}|{8}|{9} 
    --- --- --- 
    """
    print(board)

  def printBoard(self):
    board = """
    --- --- --- 
     {0} | {1} | {2} 
    --- --- --- 
     {3} | {4} | {5} 
    --- --- --- 
     {6} | {7} | {8} 
    --- --- --- 
    """ 
    board = board.format(
                  self.board[0],
                  self.board[1],
                  self.board[2],
                  self.board[3],
                  self.board[4],
                  self.board[5],
                  self.board[6],
                  self.board[7],
                  self.board[8])
    print(board)

  def placeMark(self, pos, mark):
    if (not isinstance(pos, int)):
      pos = int(pos)
    if (pos < 1 or pos > 9 or 
      self.board[pos - 1] != ' '):
      print("Not a valid position. Try again.")
      pos = input("Make your move [1 - 9]: ")
      self.placeMark(pos, mark)
    else:
      # 1/4 chance of mark not placed
      placed = random.randint(0, 3)
      if (placed >= 1):
        self.board[pos - 1] = mark
        if (mark == US):
          self.userMoves.add(pos)
        else :
          self.comMoves.add(pos)
        self.markCount += 1
        return True
      else:
        print("LOST MOVE")
        return False

  def userPlays(self):
    pos = input("Make your move [1 - 9]: ")
    placed = self.placeMark(pos, US)
    print("User has made the move: ")
    # Print message if mark not placed
    if (not placed):
      print("User's mark not placed! :(")
    self.printBoard()
    self.checkGameEnd(US)
    if (self.result == ""):
      self.comPlays()

  def comPlays(self):
    pos = random.randint(1, 9)
    if (self.board[pos - 1] != ' '):
      self.comPlays()
    else:
      placed = self.placeMark(pos, CO)
      print("Com has made the move: ")
      # Print message if mark not placed
      if (not placed):
        print("Com's mark not placed! :(")
      self.printBoard()
      self.checkGameEnd(CO)
      if (self.result == ""):
        self.userPlays()

  def checkGameEnd(self, lastMove):
    # All occupied
    if (self.markCount == 9):
      self.result = "tie"
    if (lastMove == US):
      for set in WINNING_SETS:
        if set.issubset(self.userMoves):
          self.result = "win"
    else:
      for set in WINNING_SETS:
        if set.issubset(self.comMoves):
          self.result = "lose"
    return
    
  def printResult(self):
    if (self.result == "tie"):
      print("Game ends in a tie!")
    else:
      print("You " + self.result + "!")
    return
      
  # Main game code
  def playGame(self):
    self.printBoardAtStart()
    self.userPlays()
    self.printResult()


# Main app code
playing = True

while playing:
  print("----- CHANCE TIC TAC TOE -----")
  ticTacToe = TicTacToe()
  ticTacToe.playGame()

  # Wait for user input to quit game or play again
  ans = ''
  while (ans != 'N' and ans != 'Y'):
    ans = input("Play again? Y/N\n")
  if (ans == 'N'):
    playing = False

print("--- THANKS FOR PLAYING! ---")
