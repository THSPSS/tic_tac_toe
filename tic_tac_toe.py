"""

This class is for creating TicTacToe game

it has functions that related to convey TicTacToe game


"""


class TicTacToe:



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

    #display the board
    def displayBoard(self, board_range):
        dispaly_board = ""
        for i in range(board_range):
            for j in range(board_range) :
                dispaly_board += "---- "
            dispaly_board += "\n"

        return dispaly_board

    def displayBoardAfterInsert(self,  board_list):
        dispaly_board = ""
        for i in range(len(board_list)):
            for j in range(len(board_list[i])):
                if board_list[i][j] != "-":
                    dispaly_board += f" {board_list[i][j]}  "
                else:
                    dispaly_board += "---- "
            dispaly_board += "\n"

        return dispaly_board



    def validateUserInput(self, player_input):
        if len(player_input) != 2:
            return False

        return True

    def validateInput(self, player_one_input):
        player_one_input = player_one_input.upper()

        if player_one_input not in ["O", "X"]:
            return False

        return player_one_input

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

        #print(player_input_dict)

        if not board[player_input_dict['row']][player_input_dict['column']]:
            return True
        return False

    def insertingBoard(self, board_list, player_side, row, column):
        updated_board = [row[:] for row in board_list]
        updated_board[row][column] = player_side

        return updated_board

    def inspectingBoard(self,board_list):
        count_x = 0
        count_o = 0
        for i in range(len(board_list)):
            for j in range(len(board_list[i])):
                if board_list[i][j] == "X" :
                    count_x += 1
                else:
                    count_o += 1
            if count_x == 3 and count_o == 3:
                return "It's draw!"
            elif count_o == 3:
                return "Winner is O"
            elif count_x == 3:
                return "Winner is X"
            else:
                return "There is no result yet"




