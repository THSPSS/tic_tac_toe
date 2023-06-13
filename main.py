from tic_tac_toe import TicTacToe


tictactoe = TicTacToe()


#setting game
board_game_is_on = False
player_one = None
board_num = 3

#after making board board_game_is_on set True
board_game_is_on = True


#Initialize input_not_validated variable
input_not_validated = True


#making board
board = tictactoe.makingANewBoard(board_num=board_num)
display_board = tictactoe.displayBoard(board_range=board_num)


print(display_board)



#display board to users



# Get user input
user_input = input("Please enter first player's position. O or X ? : ")



# While loop for validating user input
while input_not_validated :

    # Validate player_one input
    validate_result = tictactoe.validateInput(player_one_input=user_input)

    if validate_result is not None and not validate_result:
        print("Invalidate input.\n")
        user_input = input("Please enter first player's position. O or X ? : ")
    else:
        input_not_validated = False

player_one = validate_result
player_two = tictactoe.setOtherPlayer(first_player_input=player_one)

print(f"first player : {player_one} \nother player: {player_two}")

#couting the number to find which user playing
turn_count = 1

while board_game_is_on:

    #checking user_position with turn_count
    if turn_count % 2 != 0 :
       player_side = player_one
    else:
       player_side = player_two


    #board printing
    print(board)

    #change number to start with 1 not 0
    player_input = input("Please input your choice as [row][column] like 11 or 12 : ")

    checkUserInput = tictactoe.validateUserInput(player_input=player_input)

    if not checkUserInput :
        player_input = input("Please input your choice as [row][column] like 01 or 02")

    checkBoard = tictactoe.checkWholeBoard(board=board , row=int(player_input[0]) ,column=int(player_input[1]))

    if not checkBoard :
        player_input = input("that place already be chosen. Please choose empty space : ")

    print(checkBoard)
    #player_input = tictactoe.player_input(playerInput=player_input)

    board = tictactoe.insertingBoard(board_list=board, player_side=player_side , row=int(player_input[0]) , column=int(player_input[1]) )
    display_board = tictactoe.displayBoardAfterInsert(board_list=board)

    print(display_board)
    #if one player is turn count 3 than checking board
    #brute Force
    if turn_count >= 5:
        result = tictactoe.inspectingRow(board_list=board)
        resultCol = tictactoe.inspectingCol(board_list=board)
        #if result has no winner or draw than game is on loop
        if result != "There is no result yet":
            board_game_is_on = False
        if resultCol != "There is no result yet" :
            board_game_is_on = False


    #check if there are bingo
    #inspecting board




    turn_count += 1


