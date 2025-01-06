# Python implementation of tic tac toe
# Game is played from the command line

# ***** From Clever Programmer on YouTube *****


# -------------- Global Variables -------------- 

# Game board. Initially empty. Empty spaces signified by "-" symbol
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# Whether the game is still goind. The game ends when someone has won or it has ended in a tie
game_still_going = True

# The winner of the game. The winner if none if the game hasn't ended or has ended in a tie
winner = None

# Current player's turn
current_player = "X"

# Number of spaces filled
spaces_filled = 0



# -------------- Functions -------------- 
# Carries out the game
def play_game():
  # Global variables
  global game_still_going
  global current_player

  while game_still_going:
    display_board()
    handle_turn(current_player)
    check_if_game_over()
    current_player = flip_player(current_player)

  # The game has ended
  display_board()
  if winner == "X" or winner == "O":
    print(winner + " won.")
  else:
    print("Tie.")


# Displays the current game board. 
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


# Handles one turn of the game
def handle_turn(current):
  # Global variables
  global spaces_filled

  go = True
  while go:
    print(current + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # The user has entered an invalid position (string or num not between 1-9)
    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      print("Invalid input. Please try again.")

    else:
      position = int(position) - 1
      # Position is empty
      if board[position] == "-":
        board[position] = current
        spaces_filled += 1
        go = False
      # User selected position that is already occupied
      else:
        print("Position occupied. Try again.")


# Determines if the game has ended (Someone won or there is a tie)
def check_if_game_over():
  check_if_win()
  check_if_tie()


# Determines if someone has won the game
def check_if_win():
  # Global variables
  global winner
  global game_still_going

  # Checks if there is a winner. A winner is either three across, three down, or three diagonally
  row_winner = check_rows() 
  column_winner = check_columns() 
  diagonal_winner = check_diagonals()

  # Sets the winner of the game
  if row_winner:
    winner = row_winner
    game_still_going = False
  elif column_winner:
    winner = column_winner
    game_still_going = False
  elif diagonal_winner:
    winner = diagonal_winner
    game_still_going = False
  # No one has won yet
  else:
    winner = None


# Checks if someone has won across
def check_rows():
  if board[0] == board[1] == board[2] != "-":
    return board[0]
  elif board[3] == board[4] == board[5] != "-":
    return board[3]
  elif board[6] == board[7] == board[8] != "-":
    return board[6]
  return


# Checks if someone has won up/down
def check_columns():
  if board[0] == board[3] == board[6] != "-":
    return board[0]
  elif board[1] == board[4] == board[7] != "-":
    return board[1]
  elif board[2] == board[5] == board[8] != "-":
    return board[2]
  return 


# Checks if someone has won diagonally
def check_diagonals():
  if board[0] == board[4] == board[8] != "-":
    return board[0]
  elif board[2] == board[4] == board[6] != "-":
    return board[2]
  return


# Checks if there is a tie. There is a tie if the game board is filled and no one has won
def check_if_tie():
  global game_still_going
  global spaces_filled
  if (not check_if_win()) and (spaces_filled == 9):
    game_still_going = False
    return True
  return False


# Flips player's turn
def flip_player(current):
  if current == "X":
    return "O"
  return "X"

play_game()
