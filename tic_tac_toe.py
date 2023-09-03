"""

This class is for creating TicTacToe game

it has functions that related to convey TicTacToe game


with Minmax Algorithm


"""


class TicTacToe:

    def __init__(self):
        self.board = []



    def set_other_player(self, first_player_input):
        if first_player_input == "O":
            return "X"
        else:
            return "O"

    # creating board
    # 3 * 3 board
    # [[1 , '' , '', ] ,[1 , '' , '', ],[1 , '' , '', ]]
    # because it multiply same row , when it is called as [0][0] , other row is also called out
    def making_a_new_board(self, board_num):
        row, col = board_num, board_num
        board_list = [[""] * col for _ in range(row)]
        count = 1
        for i in range(3):
            for j in range(3) :
                board_list[i][j] = count
                count += 1

        return board_list

    def check_whole_board(self, board: object) -> object:
        for row in board:
            for item in row:
                if item in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return False
                return True

    def check_the_space(self, board: object , row: int , column: int) -> object:
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
            return False



    def validate_input(self, player_one_input):
        player_one_input = player_one_input.upper()

        if player_one_input not in ["O", "X"]:
            return False

        return player_one_input


    def player_input(self, player_inputs):
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

    def is_input_board_empty(self, player_input, board):
        # player_input_dict = self.player_input(playerInputs=player_input)
        player_input_dict = player_input

        if not board[player_input_dict['row']][player_input_dict['column']]:
            return True
        return False

    def inserting_board(self, board_list, player_side, input):
        updated_board = [row[:] for row in board_list]
        updated_board[input[0]][input[1]] = player_side

        return updated_board


    def check_for_result(self, board_list: object, cur_player: object) -> object:

        n = len(board_list)

        #inspecitng rows
        for i in range(n):
            result = True
            for j in range(n):
                if board_list[i][j] != cur_player:
                    result = False
                    break

            if result:
                return result


        #inspecting columns
        for i in range(n):
            result = True
            for j in range(n):
                if board_list[j][i] != cur_player:
                    result = False
                    break
            if result:
                return result


        #inspecting diagnols
        result = True
        for i in range(n):
            if board_list[i][i] != cur_player:
                result = False
                break
        if result:
            return result

        result = True
        for i in range(n):
            if board_list[i][n-1-i] != cur_player:
                result = False
                break
        if result:
            return result
        return False

        # for row in board_list:
        #     for item in row:
        #         if int(item) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        #             return False
        # return True



    def inspecting_row(self,board_list):
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


    def inspecting_col(self , board_list):
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

    def inspecting_diag(self , board_list):
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

    def inspecting_revers_diag(self, board_list):
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

    def check_for_win(self,board):
        result = self.inspecting_row(board_list=board)
        resultCol = self.inspecting_col(board_list=board)
        resultDiag = self.inspecting_diag(board_list=board)
        resultRevDiag = self.inspecting_revers_diag(board_list=board)

        return result , resultCol , resultDiag , resultRevDiag

    # def check_for_board_game_on(self, row_result, col_result, result_diag, result_rev_diag):
    #     if row_result != "There is no result yet" \
    #             or col_result != "There is no result yet" \
    #             or result_diag != "There is no result yet"\
    #             or result_rev_diag != "There is no result yet":
    #         return False
    #
    #     return True

    def check_for_board_game_on(self, row_result, col_result, result_diag, result_rev_diag):
        results = [row_result, col_result, result_diag, result_rev_diag]
        return not any(result != "There is no result yet" for result in results)







