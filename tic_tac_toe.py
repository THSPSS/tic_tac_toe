#making class that creating tic_tac_toe



class TicTacToe :

    def __init__(self):
        self.message = "Please select Player 1's position. X or O ?"

    # create tic tac toe game
    # get user's position
    def makingUpperCase(userInput):
        upperCase = userInput.upper()
        return upperCase

    # creating board
    # 3 * 3 board
    def makingBoard(board_num):
        board_list = []
        for i in range(0 ,board_num):
            inserted_list = []
            for j in range(0, board_num) :
                 inserted_list.append(" ")
            board_list.append(inserted_list)

        return board_list

    def player_input(self,playerInput):
        place = playerInput
        column = place[0]
        row = place[1]
        #value = list[column][row]

        return "column is {}, row is {}".format(column , row)









