"""

This class is for creating TicTacToe game

it has functions that related to convey TicTacToe game


"""


class TicTacToe:



    def set_other_player(self, first_player_input):
        if first_player_input == "O":
            return "X"
        else:
            return "O"

    # creating board
    # 3 * 3 board
    # [[1 , '' , '', ] ,[1 , '' , '', ],[1 , '' , '', ]]
    # because it multiply same row , when it is called as [0][0] , other row is also called out
    def making_a_new_Board(self, board_num):
        row, col = board_num, board_num
        board_list = [[""] * col for _ in range(row)]
        count = 1
        for i in range(3):
            for j in range(3) :
                board_list[i][j] = count
                count += 1

        return board_list

    def check_whole_board(self, board, row, column):
        if board[row][column] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            # return False which is board is not empty
            return False
        # otherwise , return True which indicate that board is empty
        return True

    #display the board
    def display_board(self, board_range ,board_list):
        display_board = ""
        for i in range(board_range):
            for j in range(board_range) :
                display_board += f" {str(board_list[i][j])} "
                if j < board_range - 1:
                    display_board += "|"
            display_board += "\n"
            if i < board_range - 1:
                display_board += "------------\n"

        return display_board

    def display_board_after_insert(self,  board_list):
        count = 1
        display_board = ""
        for i in range(len(board_list)):
            for j in range(len(board_list)) :
                display_board += f" {board_list[i][j]} "
                if j < len(board_list) - 1:
                    display_board += "|"
                count += 1
            display_board += "\n"
            if i < len(board_list) - 1:
                display_board += "------------\n"

        return display_board



    def validate_user_input(self, player_input):
        try:
            user_input = int(player_input)
            if user_input in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return True
            else:
                return False

        except ValueError:
            return "please enter number"



    def validate_input(self, player_one_input):
        player_one_input = player_one_input.upper()

        if player_one_input not in ["O", "X"]:
            return False

        return player_one_input


    def playerInput(self, player_inputs):
        userInput = ""
        user_hash = {
            "1": (0, 0),
            "2": (0, 1),
            "3": (0, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "7": (2, 0),
            "8": (2, 1),
            "9": (2, 2)
        }

        try :
            userInput = user_hash[player_inputs]
        except KeyError :
            return "please enter number from 1 to 9"

        return userInput

    def isInputBoardEmpty(self, player_input, board):
        # player_input_dict = self.player_input(playerInputs=player_input)
        player_input_dict = player_input

        if not board[player_input_dict['row']][player_input_dict['column']]:
            return True
        return False

    def insertingBoard(self, board_list, player_side, input):
        updated_board = [row[:] for row in board_list]
        updated_board[input[0]][input[1]] = player_side

        return updated_board

    def inspectingRow(self,board_list):
        result = "There is no result yet"

        for i in range(len(board_list)):
            count_x = 0
            count_o = 0
            for j in range(len(board_list)):
                if board_list[i][j] == "X" :
                    count_x += 1
                elif board_list[i][j] == "O" :
                    count_o += 1
            if count_o == 3:
                return "Winner is O"
            elif count_x == 3:
                return "Winner is X"

        return result


    def inspectingCol(self , board_list):
        result = "There is no result yet"

        for i in range(len(board_list)):
            count_x = 0
            count_o = 0
            for j in range(len(board_list)):
                if board_list[j][i] == "X" :
                    count_x += 1
                elif board_list[j][i] == "O":
                    count_o += 1
            if count_o == 3:
                return "Winner is O"
            elif count_x == 3:
                return "Winner is X"

        return result

    def inspectingDiag(self , board_list):
        result = "There is no result yet"
        count_x = 0
        count_o = 0
        for i in range(len(board_list)):
            if board_list[i][i] == "X":
                count_x += 1
            elif board_list[i][i] == "O":
                count_o += 1
        if count_o == 3:
            return "Winner is O"
        elif count_x == 3:
            return "Winner is X"

        return result

    def inspectingReversDiag(self, board_list):
        result = "There is no result yet"
        count_x = 0
        count_o = 0

        for i in range(len(board_list)-1 , -1, -1):
            if board_list[(len(board_list)-1)-i][i] == "X":
                count_x += 1
            elif board_list[(len(board_list)-1)-i][i] == "O":
                count_o += 1

        if count_o == 3:
            return "Winner is O"
        elif count_x == 3:
            return "Winner is X"

        return result

    def check_for_Win(self,board):
        result_for_checking = ""
        result = self.inspectingRow(board_list=board)
        resultCol = self.inspectingCol(board_list=board)
        resultDiag = self.inspectingDiag(board_list=board)
        resultRevDiag = self.inspectingReversDiag(board_list=board)

        return result , resultCol , resultDiag , resultRevDiag

    def check_for_board_game_on(self, row_result, col_result, result_diag, result_rev_diag):
        if (row_result or col_result or result_diag or result_rev_diag) != "There is no result yet":
            return False

        return True






