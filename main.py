from tic_tac_toe import TicTacToe

def play_tic_tac_toe():
    tictactoe = TicTacToe()

    board_num = 3
    #board_game_is_on = True

    #Initialize input_not_validated variable
    input_not_validated = True

    #making board
    board = tictactoe.making_a_new_board(board_num=board_num)
    display_board = tictactoe.display_board(board_range=board_num , board_list=board)

    # Get user input
    user_input = input("Please enter first player's position. O or X ? : ")

    #display board to users
    print(display_board)


    # While loop for validating user input
    while input_not_validated :

        # Validate player_one input
        validate_result = tictactoe.validate_input(player_one_input=user_input)

        if validate_result is not None and not validate_result:
            print("Invalidate input.\n")
            user_input = input("Please enter first player's position. O or X ? : ")
        else:
            input_not_validated = False

    player_one = validate_result
    player_two = tictactoe.set_other_player(first_player_input=player_one)
    print(f"first player : {player_one} \nother player: {player_two}")

    #board printing
    print(board)
    turn_count = 1
    while True:

        # couting the number to find which user playing


        # checking user_position with turn_count
        if turn_count % 2 != 0:
            player_side = player_one
        else:
            player_side = player_two


        while True:
            #change number to start with 1 not 0
            player_input = input("Please enter your choice from 1 to 9 : ")
            if tictactoe.validate_user_input(player_input=player_input):
                break
            else:
                print("Invalid input , please try again")

        player_input = tictactoe.player_input(player_inputs = player_input)

        check_the_board = tictactoe.check_the_space(board=board , row=int(player_input[0]) ,column=int(player_input[1]))

        if not check_the_board :
            player_input = input("that place already be chosen. Please choose empty space : ")

        print(check_the_board)

        board = tictactoe.inserting_board(board_list=board, player_side=player_side , input = player_input)
        display_board = tictactoe.display_board_after_insert(board_list=board)

        print(display_board)

        # result , result_col , result_diag , result_rev_diag = tictactoe.check_for_win(board=board)
        # board_game_is_on = tictactoe.check_for_board_game_on(result , result_col , result_diag , result_rev_diag)
        #
        #
        # print(result)
        # print(result_col)
        # print(result_diag)
        # print(result_rev_diag)
        check_result = tictactoe.check_for_result(board_list=board , cur_player= player_side)
        if check_result :
            print(f"Player {player_side} win")
            break

        check_draw = tictactoe.check_whole_board(board=board)
        if check_draw:
            print("It is a Draw")
            break

        #check if there are bingo
        #inspecting board
        #showing result about the scores

        turn_count += 1



play_tic_tac_toe()


