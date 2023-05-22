import unittest

from tic_tac_toe import TicTacToe as ttt


class TestTicTacToe(unittest.TestCase):

    #def test_gettingUserPosition(self):
    #    self.assertEqual(ttt.getting_user_position())

    def test_makingUpperCaseX(self):
        self.assertEqual(ttt.makingUpperCase("x"),'X')

    def test_makingUpperCaseO(self):
        self.assertEqual(ttt.makingUpperCase("o"),'O')





