from tic_tac_toe import TicTacToe

#setting game
board_game_is_on = False



tictactoe = TicTacToe()



board = tictactoe.makingANewBoard(board_num=3)

#after setting board board_game_is_on set True

board_game_is_on = True


user_input = input("Please enter first player's position. O or X ? : ")


player_one = tictactoe.makingUpperCase(userInput=user_input)
player_two = tictactoe.setOtherPlayer(first_player_input=player_one)

print(f"first player : {player_one} \nother player: {player_two}")

play_times = 1

while board_game_is_on:

    if play_times % 2 != 0 :
       player_side = player_one
    else:
       player_side = player_two


    print(board)

    player_input = input("Please input your choice as [row][column] like 11 or 12 : ")

    checkUserInput = tictactoe.checking_user_input(playerInputs=player_input)

    if not checkUserInput :
        player_input = input("Please input your choice as [row][column] like 01 or 02")

    checkBoard = tictactoe.checkingIfBoardFilled(board=board , row=int(player_input[0]) ,column=int(player_input[1]))

    if not checkBoard :
        player_input = input("that place already be chosen. Please choose empty space : ")

    print(checkBoard)
    #player_input = tictactoe.player_input(playerInput=player_input)

    board = tictactoe.inserting_board(board_list=board, player_side=player_side , row=int(player_input[0]) , column=int(player_input[1]) )

    output_result = "After input Board : {}".format(board)
    print(output_result)

    play_times += 1


