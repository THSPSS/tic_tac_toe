"""

This class is for creating TicTacToe game

it has functions that related to convey TicTacToe game


"""


class TicTacToe:


    #UpperCase user input
    def makingUpperCase(self, user_input):
        upper_case = user_input.upper()
        return upper_case

    def setOtherPlayer(self, first_player_input):
        if first_player_input == "O":
            return "X"
        else:
            return "O"

    # creating board
    # 3 * 3 board
    def makingANewBoard(self, board_num):
        row, col = board_num, board_num
        board_list = [["-"] * col] * row

        return board_list

    def checkWholeBoard(self, board, row, column):
        if board[row][column] != "-":
            # return False which is board is not empty
            return False
        # otherwise , return True which indicate that board is empty
        return True

    def validateUserInput(self, player_input):
        if len(player_input) != 2:
            return False
        # and playerInputs[0] == "o" or "x" and int(playerInputs[1]) <= 9 and int(playerInputs[2]) <= 9:
        return True

    def validateInput(self, player_one_input):
        if player_one_input not in ["O", "X"]:
            return False

        return True

    def playerInput(self, player_inputs):
        place = player_inputs
        row = place[0]
        column = place[1]
        # value = list[column][row]

        # return "player {} column is {}, row is {}".format(player_side ,column , row)
        return row, column

    def isInputBoardEmpty(self, player_input, board):
        # player_input_dict = self.player_input(playerInputs=player_input)
        player_input_dict = player_input

        print(player_input_dict)

        if not board[player_input_dict['row']][player_input_dict['column']]:
            return True
        # board[player_input_dict['row']][player_input_dict['column']] = player_input_dict["player_side"]

        return False

    def insertingBoard(self, board_list, player_side, row, column):
        updated_board = [row[:] for row in board_list]
        print(f"this is player side : {player_side}")
        print("this is the board", board_list)
        print(f"user inset on this place updated_board[{row}][{column}]")
        updated_board[row][column] = player_side

        return updated_board
