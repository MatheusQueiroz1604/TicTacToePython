import random


def display_board(board):
  # The function accepts one parameter containing the board's current status
  # and prints it out to the console.
  for row in board:
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
  # The function accepts the board current status, asks the user about their move,
  # checks the input and updates the board according to the user's decision.
  free_fields = make_list_of_free_fields(board)

  while True:
    user_move = input("Enter your move: ")
    if user_move.isdigit():
      user_move = int(user_move)
      if user_move < 1 or user_move > 9:
        print("Invalid input! Please enter a number between 1 and 9.")
        continue
      row = (user_move - 1) // 3
      col = (user_move - 1) % 3
      if (row, col) not in free_fields:
        print("That square is already taken! Please choose another.")
        continue
      else:
        board[row][col] = 'O'
        break
    else:
      print("Invalid input! Please enter a number.")


def make_list_of_free_fields(board):
  # The function browses the board and builds a list of all the free squares;
  # the list consists of tuples, while each tuple is a pair of row and column numbers.
  free_fields = []
  for row in range(3):
    for col in range(3):
      if board[row][col] != 'X' and board[row][col] != 'O':
        free_fields.append((row, col))
  return free_fields


def victory_for(board, sign):
  # The function analyzes the board status in order to check if
  # the player using 'O's or 'X's has won the game
  for row in board:
    if row[0] == row[1] == row[2] == sign:
      return True

  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] == sign:
      return True

  if board[0][0] == board[1][1] == board[2][2] == sign:
    return True

  if board[0][2] == board[1][1] == board[2][0] == sign:
    return True

  return False


def draw_move(board):
  # The function draws the computer's move and updates the board.
  free_fields = make_list_of_free_fields(board)

  while True:
    row, col = random.choice(free_fields)
    if board[row][col] == 'X' or board[row][col] == 'O':
      continue
    else:
      board[row][col] = 'X'
      break


board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

while True:
  draw_move(board)
  display_board(board)

  if victory_for(board, 'X'):
    print("You lost!")
    break

  if len(make_list_of_free_fields(board)) == 0:
    display_board(board)
    print("It's a draw!")
    break

  enter_move(board)

  if victory_for(board, 'O'):
    display_board(board)
    print("You won!")
    break