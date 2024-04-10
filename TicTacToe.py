'''
Simple Tic Tac Toe Game
'''
import random
from TTTFunc import display_board, player_input, place_marker, win_check, choose_first, space_check, full_board_check, player_choice, replay


def main():
  

  while True:
      print('Welcome to Tic Tac Toe!')
      theBoard = [' '] * 10
      player1_marker, player2_marker = player_input() 
      turn = choose_first()
      print(turn + ' will go first.')
      
      play_game = input('Are you ready to play? Enter Yes or No. ')
      
      if play_game.lower()[0] == 'y':
          game_on = True
      else:
          game_on = False

      while game_on:
          if turn == 'Player 1':
              # Player1's turn.
              
              display_board(theBoard)
              position = player_choice(theBoard)
              place_marker(theBoard, player1_marker, position)

              if win_check(theBoard, player1_marker):
                  display_board(theBoard)
                  print('Player 1 has won the game!')
                  game_on = False
              else:
                  if full_board_check(theBoard):
                      display_board(theBoard)
                      print("It's a draw!")
                      break
                  else:
                      turn = 'Player 2'

          else:
              # Player2's turn.
              
              display_board(theBoard)
              position = player_choice(theBoard)
              place_marker(theBoard, player2_marker, position)

              if win_check(theBoard, player2_marker):
                  display_board(theBoard)
                  print('Player 2 has won the game!')
                  game_on = False
              else:
                  if full_board_check(theBoard):
                      display_board(theBoard)
                      print("It's a draw!")
                      break
                  else:
                      turn = 'Player 1'

      if not replay():
          break



if __name__ == '__main__':
    main()