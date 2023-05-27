#making class that creating tic_tac_toe



class TicTacToe :

    # def __init__(self):
    #     self.message = "Please select Player 1's position. X or O ?"

    # create tic tac toe game
    # get user's position
    def makingUpperCase(userInput):
        upperCase = userInput.upper()
        return upperCase

    # creating board
    # 3 * 3 board
    def makingANewBoard(self,board_num):
        board_list = []
        for i in range(0 ,board_num):
            inserted_list = []
            for j in range(0, board_num) :
                 inserted_list.append("-")
            board_list.append(inserted_list)

        return board_list

    def checkingIfBoardFilled(board):
        for list in board :
            for element in list :
                #if board has something other than - mark
                if element != "-" :
                    #return False which is board is not empty
                    return False
        #otherwise , return True which indicate that board is empty
        return True

    def player_input(self,playerInput):
        place = playerInput
        player_side = place[0]
        column = place[1]
        row = place[2]
        #value = list[column][row]

        return "player {} column is {}, row is {}".format(player_side ,column , row)


    def inserting_board( board_list , player_side ,column , row):
        board_list[row][column] = player_side

        return board_list










