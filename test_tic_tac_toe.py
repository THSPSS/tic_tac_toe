import unittest

from tic_tac_toe import TicTacToe as ttt


class TestTicTacToe(unittest.TestCase):

    #def test_gettingUserPosition(self):
    #    self.assertEqual(ttt.getting_user_position())

    def test_makingUpperCaseX(self):
        self.assertEqual(ttt.makingUpperCase("x"),'X')

    def test_makingUpperCaseO(self):
        self.assertEqual(ttt.makingUpperCase("o"),'O')


    # def test_making_board_checking_number(self):
    #     self.assertEqual(ttt.makingBoard(3),'3')

    def test_making_board_checking_board_list(self):
        self.assertEqual(ttt.makingANewBoard(3), [["-","-","-"],["-","-","-"],["-","-","-"]])


    def test_player_input(self):
        self.assertEqual(ttt.player_input(self,"O11"), "player O column is 1, row is 1")

    def test_inserting_board(self):
        self.assertEqual(ttt.inserting_board(board_list=[["-","-","-"],["-","-","-"],["-","-","-"]], player_side="O" , column=1, row=2),
                         [["-","-","-"],["-","-","-"],["-","O","-"]])

    def test_checking_if_board_is_empty(self):
        self.assertTrue(ttt.checkingIfBoardFilled([["-","-","-"],["-","-","-"],["-","-","-"]]))

    def test_checking_if_board_is_not_empty(self):
        self.assertFalse(ttt.checkingIfBoardFilled([["O","-","-"],["O","-","-"],["O","-","-"]]))




