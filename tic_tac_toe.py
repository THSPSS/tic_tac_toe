#making class that creating tic_tac_toe



class TicTacToe :

    # def __init__(self):
    #     self.message = "Please select Player 1's position. X or O ?"

    # create tic tac toe game
    # get user's position
    def makingUpperCase(self , userInput):
        upperCase = userInput.upper()
        return upperCase

    def setOtherPlayer(self, first_player_input):
        if first_player_input == "O":
            return "X"
        else:
            return "O"

    # creating board
    # 3 * 3 board
    def makingANewBoard(self,board_num):
        row , col = board_num , board_num
        board_list = [["-"]*col]*row
        # for i in range(0 ,board_num):
        #     inserted_list = []
        #     for j in range(0, board_num) :
        #          inserted_list.append("-")
        #     board_list.append(inserted_list)

        return board_list

    def checkingIfBoardFilled(self , board , row , column):
        if board[row][column] != "-" :
            #return False which is board is not empty
            return False
        #otherwise , return True which indicate that board is empty
        return True

    def checking_user_input(self , playerInputs):
        print(len(playerInputs))
        if len(playerInputs) != 2 :
            return False
        #and playerInputs[0] == "o" or "x" and int(playerInputs[1]) <= 9 and int(playerInputs[2]) <= 9:
        return True


    def player_input(self,playerInputs):
        place = playerInputs
        row = place[0]
        column = place[1]
        #value = list[column][row]

        #return "player {} column is {}, row is {}".format(player_side ,column , row)
        return row , column

    def isInputBoardEmpty(self , playerInput , board):
        #playerInputDict = self.player_input(playerInputs=playerInput)
        playerInputDict = playerInput

        print(playerInputDict)


        if not board[playerInputDict['row']][playerInputDict['column']] :
            return True
        #board[playerInputDict['row']][playerInputDict['column']] = playerInputDict["player_side"]


        return False


    def inserting_board( self , board_list , player_side , row , column):
        updated_board = [row[:] for row in board_list]
        print(f"this is plyar side : {player_side}")
        print("this is the board",board_list)
        print(f"user inset on this place boardlist[{row}][{column}]")
        updated_board[row][column] = player_side

        return updated_board










