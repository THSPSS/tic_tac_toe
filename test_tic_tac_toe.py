import unittest

from tic_tac_toe import TicTacToe as ttt


class TestTicTacToe(unittest.TestCase):

    #def test_gettingUserPosition(self):
    #    self.assertEqual(ttt.getting_user_position())

    def test_set_other_player_when_O(self):
        self.assertEqual(ttt.setOtherPlayer(self,"O"),"X")

    def test_set_other_player_when_X(self):
        self.assertEqual(ttt.setOtherPlayer(self,"X"),"O")


    def test_making_board(self):
        self.assertEqual(ttt.makingANewBoard(self,board_num=3), [["-","-","-"],["-","-","-"],["-","-","-"]])


    # def test_checking_user_input_length(self):
    #     self.assertFalse(ttt.checking_user_input(self,"o1"))


    def test_player_input(self):
        self.assertEqual(ttt.playerInput(self,"11"), ("1","1"))


    def test_inserting_board(self):
        self.assertEqual(ttt.insertingBoard(self ,
                                             board_list=[["-","-","-"],["-","-","-"],["-","-","-"]],
                                             player_side="O" ,
                                             row=2 ,
                                             column=0),
                         [["-","-","-"],["-","-","-"],["O","-","-"]])

    def test_checking_if_board_is_empty(self):
        self.assertTrue(ttt.checkWholeBoard(self ,[["-","-","-"],["-","-","-"],["-","-","-"]],row=0, column=0))

    def test_checking_whole_board_is_not_empty(self):
        self.assertFalse(ttt.checkWholeBoard(self,board=[["O","-","-"],["","-","-"],["","-","-"]],row=0,column=0))

    def test_board_is_empty_or_not(self):
        self.assertFalse(ttt.isInputBoardEmpty(self,player_input={ "player_side" : "O" , "column" : 1 , "row" : 1},board=[["-","-","-"],["-","O","-"],["O","-","-"]]))

    def test_validateInput_empty_string(self):
        self.assertFalse(ttt.validateInput(self,player_one_input=""))

    def test_validateInput_number(self):
        self.assertFalse(ttt.validateInput(self,player_one_input="1"))

    def test_validateInput_typo(self):
        self.assertFalse(ttt.validateInput(self,player_one_input="ㅇ"))

    def test_validateInput_True(self):
        self.assertTrue(ttt.validateInput(self,player_one_input="X"))

    #test display board
    def test_displayBoard(self):
        self.assertEqual(ttt.displayBoard(self,3),
                         "---- ---- ---- \n"
                         "---- ---- ---- \n"
                         "---- ---- ---- \n")


    def test_displayBoardAfterInsert(self):
        self.assertEqual(ttt.displayBoardAfterInsert(self))