from tic_tac_toe import TicTacToe


tictactoe = TicTacToe()


#setting game
board_game_is_on = False
player_one = None
#after making board board_game_is_on set True
board_game_is_on = True
user_input_validate = False


#making board
board = tictactoe.makingANewBoard(board_num=3)
#get user input
user_input = input("Please enter first player's position. O or X ? : ")



#making while loop validating user input
while not user_input_validate :
    player_one = tictactoe.makingUpperCase(user_input=user_input)

#validate player_one input
    user_input_validate = tictactoe.validateInput(player_one_input=player_one)
#what if user put false input such as 1 or ohter gibbelish word?


player_two = tictactoe.setOtherPlayer(first_player_input=player_one)

print(f"first player : {player_one} \nother player: {player_two}")

turn_count = 1

while board_game_is_on:

    #checking user_position with turn_count
    if turn_count % 2 != 0 :
       player_side = player_one
    else:
       player_side = player_two


    #board printing
    print(board)

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

    output_result = "After input Board : {}".format(board)
    print(output_result)

    turn_count += 1


