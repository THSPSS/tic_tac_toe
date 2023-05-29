from tic_tac_toe import TicTacToe

tictactoe = TicTacToe()

board = tictactoe.makingANewBoard(board_num=3)

print(board)


user_input = input("Please enter your position. O or X ? ")


Player_one = tictactoe.makingUpperCase(userInput=user_input)


print(Player_one)


board_game_is_on = True

while board_game_is_on:
    player_input = input("Please input your choice as [column][row] like like o11")

    print(player_input)

    player_input = tictactoe.player_input(playerInput=player_input)

    print(player_input)


