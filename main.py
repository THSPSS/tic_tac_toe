from tic_tac_toe import TicTacToe

board_game_is_on = False


tictactoe = TicTacToe()

board = tictactoe.makingANewBoard(board_num=3)
isBoardEmpty = tictactoe.checkingIfBoardFilled(board=board)

if isBoardEmpty :
    board_game_is_on = True
    print(board)



user_input = input("Please enter first player's position. O or X ? : ")

player_one = tictactoe.makingUpperCase(userInput=user_input)

player_two = tictactoe.setOtherPlayer(first_player_input=player_one)

print(player_one)

play_times = 0

while board_game_is_on:

    if play_times % 2 != 0 :
       player_side = player_one
    else:
       player_side = player_two


    player_input = input("Please input your choice as [row][column] like 01 or 02 : ")

    print(player_input)

    checkUserInput = tictactoe.checking_user_input(playerInputs=player_input)

    if not checkUserInput :
        player_input = input("Please input your choice as [row][column] like 01 or 02")


    #player_input = tictactoe.player_input(playerInput=player_input)

    #board = tictactoe.inserting_board(board_list=board, player_side=player_side , row=int(player_input[0]) , column=int(player_input[1]) )



