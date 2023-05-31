import unittest

from tic_tac_toe import TicTacToe as ttt


class TestTicTacToe(unittest.TestCase):

    #def test_gettingUserPosition(self):
    #    self.assertEqual(ttt.getting_user_position())

    def test_makingUpperCaseX(self):
        self.assertEqual(ttt.makingUpperCase(self, userInput="x"),'X')

    def test_makingUpperCaseO(self):
        self.assertEqual(ttt.makingUpperCase(self,"o"),'O')


    # def test_making_board_checking_number(self):
    #     self.assertEqual(ttt.makingBoard(3),'3')

    def test_making_board_checking_board_list(self):
        self.assertEqual(ttt.makingANewBoard(self,board_num=3), [["-","-","-"],["-","-","-"],["-","-","-"]])


    def test_player_input(self):
        self.assertEqual(ttt.player_input(self,"O11"), { "plyer_side" : "O" , "column" : "1" , "row" : "1"})

    def test_inserting_board(self):
        self.assertEqual(ttt.inserting_board(board_list=[["-","-","-"],["-","-","-"],["-","-","-"]], player_side="O" , column=1, row=2),
                         [["-","-","-"],["-","-","-"],["-","O","-"]])

    def test_checking_if_board_is_empty(self):
        self.assertTrue(ttt.checkingIfBoardFilled(self ,[["-","-","-"],["-","-","-"],["-","-","-"]]))

    def test_checking_if_board_is_not_empty(self):
        self.assertFalse(ttt.checkingIfBoardFilled(self ,[["O","-","-"],["O","-","-"],["O","-","-"]]))

    def test_board_is_empty_or_not(self):
        self.assertFalse(ttt.isInputBoardEmpty(self,playerInput={ "player_side" : "O" , "column" : 1 , "row" : 1},board=[["-","-","-"],["-","O","-"],["O","-","-"]]))


