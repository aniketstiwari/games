import pdb

board = ['-'] * 9
winner = None
game_still_going = True
player = 'x'


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def start_game():
    display_board()

    while game_still_going:
        handle_input(player)
        check_if_game_over()
        flip_player()


    if winner == 'x' or winner == 'o':
        print(winner + ' Won')
    elif winner == None:
        print('tie')


def handle_input(player):
  print(player + "'s turn.")
    
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:
    while position not in range(1,10):
        position = input('Your input is wrong Please enter number between 1 to 9 ')

    position = int(position) - 1

    if board[position] == '-':
        valid = True
    else:
        print("Invalid input. Already exist ")

  board[position] = player
  display_board()



def check_if_game_over():
  check_if_winner()
  check_if_tie()


def flip_player():
  global player
  if player == 'x':
    player = 'o'
  elif player == 'o':
    player = 'x'
  return

def check_if_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonal()

  if row_winner:
      winner = row_winner
  elif column_winner:
      winner = column_winner
  elif diagonal_winner:
      winner = diagonal_winner
  else:
      winner = None
  return


def check_if_tie():
  global game_still_going
  if '-' not in board:
      game_still_going = False
  return

def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'

  if row_1 or row_2 or row_3:
      game_still_going = False
  if row_1:
      return board[0]
  elif row_2:
      return board[3]
  elif row_3:
      return board[6]
  return

def check_columns():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != '-'
  column_2 = board[1] == board[4] == board[7] != '-'
  column_3 = board[2] == board[5] == board[8] != '-'

  if column_1 or column_2 or column_3:
      game_still_going = False
  if column_1:
      return board[0]
  elif column_2:
      return board[1]
  elif column_3:
      return board[2]
  return

def check_diagonal():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != '-'
  diagonal_2 = board[2] == board[4] == board[6] != '-'

  if diagonal_1 or diagonal_2:
      game_still_going = False
  if diagonal_1:
      return board[0]
  elif diagonal_2:
      return board[3]
  return


start_game()