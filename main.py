from tic_tac_toe import TicTacToe

board_game_is_on = False


tictactoe = TicTacToe()

board = tictactoe.makingANewBoard(board_num=3)
isBoardEmpty = tictactoe.checkingIfBoardFilled(board=board)

if isBoardEmpty :
    board_game_is_on = True
    print(board)



user_input = input("Please enter your position. O or X ? ")


player_one = tictactoe.makingUpperCase(userInput=user_input)


print(player_one)




while board_game_is_on:
    player_input = input("Please input your choice as [column][row] like like o11")

    print(player_input)

    player_input = tictactoe.player_input(playerInput=player_input)

    print(player_input)


