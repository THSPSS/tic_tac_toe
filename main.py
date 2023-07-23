from tic_tac_toe import TicTacToe

def play_tic_tac_toe():
    tictactoe = TicTacToe()

    #setting game
    board_game_is_on = False
    player_one = None
    board_num = 3

    #after making board board_game_is_on set True
    board_game_is_on = True


    #Initialize input_not_validated variable
    input_not_validated = True


    #Replay TicTacToe game
    replay_on = True

    #making board
    board = tictactoe.making_a_new_Board(board_num=board_num)
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

    #couting the number to find which user playing
    turn_count = 1

    while board_game_is_on and replay_on :

        #checking user_position with turn_count
        if turn_count % 2 != 0 :
           player_side = player_one
        else:
           player_side = player_two


        #board printing
        print(board)

        #change number to start with 1 not 0
        player_input = input("Please enter your choice from 1 to 9 : ")

        checkUserInput = tictactoe.validate_user_input(player_input=player_input)

        if not checkUserInput :
            player_input = input("Please enter a number")

        player_input = tictactoe.player_input(player_inputs = player_input)

        checkBoard = tictactoe.check_whole_board(board=board , row=int(player_input[0]) ,column=int(player_input[1]))

        if not checkBoard :
            player_input = input("that place already be chosen. Please choose empty space : ")

        print(checkBoard)

        board = tictactoe.inserting_board(board_list=board, player_side=player_side , input = player_input)
        display_board = tictactoe.display_board_after_insert(board_list=board)

        print(display_board)

        if turn_count >= 5 and turn_count < 9:
            result , result_col , result_diag , result_rev_diag = tictactoe.check_for_win(board=board)

            print(result)
            print(result_col)
            print(result_diag)
            print(result_rev_diag)


            board_game_is_on = tictactoe.check_for_board_game_on(result , result_col , result_diag , result_rev_diag)

            #board_game_is_on is false than ended game here

            if not board_game_is_on:
                print("Game over!")

            is_replay = input("Do you want to quit this game?")

            if is_replay.upper() == 'Y':
                replay_on = False


        if turn_count == 9 :
            result, result_col, result_diag, result_rev_diag = tictactoe.check_for_win(board=board)
            is_it_end = tictactoe.check_for_board_game_on(result , result_col , result_diag , result_rev_diag)

            if is_it_end :
                print("It is draw!")


            print(result)
            print(result_col)
            print(result_diag)
            print(result_rev_diag)

            # becuase there is no space left , board game sequence is false
            board_game_is_on = False

            print("Game over!")
            is_replay = input("Do you want to quit this game?")

            if is_replay.upper() == 'Y':
                replay_on = False

        #check if there are bingo
        #inspecting board

        turn_count += 1




play_tic_tac_toe()


