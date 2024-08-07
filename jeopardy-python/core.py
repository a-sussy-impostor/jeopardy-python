class Jeopardy:
  """
  Represents a Jeopardy game board.

  Attributes:
      column: List of column titles (categories).
      row: List of row values (points).
      matrix: 2D list representing the game board, with scores.
      matrixQ: 2D list representing the game board, with questions.
      matrixA: 2D list representing the game board, with answers.
  """
  def __init__(self,row: list[str],column: list[str]):
    """
    Initializes a Jeopardy game board.

    Args:
        row: List of row values (points).
        column: List of column titles (categories).
    """
    # Initialize class properties
    self.__column = column
    self.__row = row
    self.__row2 = []
    # Create game matrix
    for __i in self.__row:
      self.__row2.append([__i] * len(self.__column))
    # Clone game matrix
    self.matrix = self.__row2 # The one with the scores
    self.matrixQ = self.__row2 # The one with the questions
    self.matrixA = self.__row2 # The one with the answers
    del column, row, self.__row

  def set_questions(self,questions: list, answers: list):
    """
    Sets the questions and answers for the game board.

    Args:
        questions: List of question lists.
        answers: List of answer lists.
    """
    self.questions = questions
    self.answers = answers
    # Resize matrixQ and matrixA to match the number of questions
    self.matrixQ = [[" " for _ in range(len(self.__column))] for _ in range(len(self.questions))]
    self.matrixA = [[" " for _ in range(len(self.__column))] for _ in range(len(self.answers))]

    for __i in range(len(self.questions)):
      self.__j = 0
      for __k in self.questions[__i]:
        self.matrixQ[__i][self.__j] = __k
        self.__j += 1
    for __i in range(len(self.answers)):
      self.__j = 0
      for __k in self.answers[__i]:
        self.matrixA[__i][self.__j] = __k
        self.__j += 1
    del self.__j

  def fetch_questions(self,questions: str, answers: str):
    """
    Fetches questions and answers from files.

    Args:
        questions: Path to the questions file.
        answers: Path to the answers file.
    """
    with open(questions,"r") as __q:
      __q2 = __q.read().split("*---*\n")
      self.__q3 = []
      for __i in __q2:
        self.__q3.append(__i.splitlines())
    with open(answers,"r") as __a:
      __a2 = __a.read().split("*---*\n")
      self.__a3 = []
      for __i in __a2:
        self.__a3.append(__i.splitlines())
    self.set_questions(self.__q3,self.__a3)

class Game:
  """
  Represents a Jeopardy game.

  Attributes:
      jeopardy: Jeopardy game board instance.
      matrix: 2D list representing the game board, with scores.
      columnTitle: List of column titles (categories).
      players: List of player names.
      playerCount: Current player's turn.
      rounds: Number of rounds remaining.
      points: List of player scores.
  """
  def __init__(self, jeopardy: Jeopardy, columnTitle: list[str], players: list[str], rounds: int):
    """
    Initializes a Jeopardy game.

    Args:
        jeopardy: Jeopardy game board instance.
        columnTitle: List of column titles (categories).
        players: List of player names.
        rounds: Number of rounds.
    """
    self.jeopardy = jeopardy
    self.matrix = self.jeopardy.matrix
    self.columnTitle = columnTitle
    self.players = players
    self.playerCount = len(players)
    self.rounds = rounds
    self.points = [0] * self.playerCount

  def show_game_board(self):
    """
    Displays the game board.
    """
    print(" ".join(self.columnTitle))
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix]))

  def gain_points(self,player: str, points: int):
    """
    Adds points to a player's score.

    Args:
        player: Name of the player.
        points: Number of points to add.
    """
    self.points[self.players.index(player)] += points

  def lose_points(self,player: str, points: int):
    """
    Subtracts points from a player's score.

    Args:
        player: Name of the player.
        points: Number of points to subtract.
    """
    self.points[self.players.index(player)] -= points

  def check_answer(self,row: int, column: int, answer: str):
    """
    Checks if the answer is correct.

    Args:
        row: Row index.
        column: Column index.
        answer: Correct answer.
    """
    return self.matrix[row][column] == answer

  def eliminate(self,player: str):
    """
    Eliminates a player from the game.

    Args:
        player: Name of the player to eliminate.
    """
    self.players.remove(player)
    self.points.pop(self.players.index(player))
    self.playerCount -= 1
    
  def show_scores(self):
    """
    Displays the current scores.
    """
    print("Current Scores:")
    for i, player in enumerate(self.players):
      print(f"{player}: {self.points[i]}")