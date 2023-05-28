from tic_tac_toe import TicTacToe

tictactoe = TicTacToe()

board = tictactoe.makingANewBoard(board_num=3)

print(board)


user_input = input("Please enter your position. O or X ? ")


Player_one = tictactoe.makingUpperCase(userInput=user_input)


print(Player_one)



