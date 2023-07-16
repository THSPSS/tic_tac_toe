import unittest

from tic_tac_toe import TicTacToe as ttt


class TestTicTacToe(unittest.TestCase):

    #def test_gettingUserPosition(self):
    #    self.assertEqual(ttt.getting_user_position())

    def test_set_other_player_when_O(self):
        self.assertEqual(ttt.set_other_player(self,"O"),"X")

    def test_set_other_player_when_X(self):
        self.assertEqual(ttt.set_other_player(self,"X"),"O")


    def test_making_a_new_board(self):
        self.assertEqual(ttt.making_a_new_Board(self,board_num=3), [[1,2,3],[4,5,6],[7,8,9]])


    # def test_checking_user_input_length(self):
    #     self.assertFalse(ttt.checking_user_input(self,"o1"))


    def test_player_input(self):
        self.assertEqual(ttt.player_input(self , "1"), (0, 0))


    def test_player_input(self):
        self.assertEqual(ttt.player_input(self , "2"), (0, 1))

    def test_player_input(self):
        self.assertEqual(ttt.player_input(self , "10"), "please enter number from 1 to 9")


    def test_inserting_board(self):
        self.assertEqual(ttt.inserting_board(self ,
                                             board_list=[[1,2,3],[4,5,6],[7,8,9]],
                                             player_side="O" ,
                                             input=(0,1)),
                         [[1,"O",3],[4,5,6],[7,8,9]])


    def test_checking_if_board_is_empty(self):
        self.assertTrue(ttt.check_whole_board(self ,[[1,2,3],[4,5,6],[7,8,9]],row=0, column=0))

    def test_checking_whole_board_is_not_empty(self):
        self.assertFalse(ttt.check_whole_board(self,board=[["O",2,3],[4,5,6],[7,8,9]],row=0,column=0))

    # def test_board_is_empty_or_not(self):
    #     self.assertFalse(ttt.is_input_board_empty(self,player_input="1",board=[["O",2,3],[4,5,6],[7,8,9]]))

    def test_validate_input_empty_string(self):
        self.assertFalse(ttt.validate_input(self,player_one_input=""))

    def test_validate_input_number(self):
        self.assertFalse(ttt.validate_input(self,player_one_input="11"))

    def test_validate_input_typo(self):
        self.assertFalse(ttt.validate_input(self,player_one_input="ㅇ"))

    def test_validate_input_True(self):
        self.assertTrue(ttt.validate_input(self,player_one_input="X"))

    def test_validate_user_input_False(self):
        self.assertFalse(ttt.validate_user_input(self,player_input="12"))

    def test_validate_user_input_True(self):
        self.assertTrue(ttt.validate_user_input(self,player_input="1"))

    def test_validate_user_input_True(self):
        self.assertEqual(ttt.validate_user_input(self,player_input="d"),"please enter number")

    #test display board
    def test_display_board(self):
        self.assertEqual(ttt.display_board(self,3, [[1,2,3],[4,5,6],[7,8,9]]),
                         " 1 | 2 | 3 \n"
                         "------------\n"
                         " 4 | 5 | 6 \n"
                         "------------\n"
                         " 7 | 8 | 9 \n")


    def test_display_boardAfterInsert(self):
        self.assertEqual(ttt.display_board_after_insert(self, board_list=[["O", "O", "O"], [4, 5, 6], ["X", 8, "X"]]),
                         " O | O | O \n"
                         "------------\n"
                         " 4 | 5 | 6 \n"
                         "------------\n"
                         " X | 8 | X \n")

    def test_inspectingRow(self):
        self.assertEqual(ttt.inspecting_row(self, board_list=[["O", "O", "O"], ["X", "X", 6], [7,8,9]]),"Winner is O")

    def test_two_inspectingRow(self):
        self.assertEqual(ttt.inspecting_row(self, board_list=[[1, "O", "O"], ["X", "X", "X"], [7, 8, 9]]),"Winner is X")

    def test_inspectingCol(self):
        self.assertEqual(ttt.inspecting_col(self,board_list=[[1,"O","X"],[3,"O","X"],[6,7,"X"]]),"Winner is X")

    def test_two_inspectingCol(self):
        self.assertEqual(ttt.inspecting_col(self,board_list=[["O","X",3],["O","X","X"],[7,"X","O"]]),"Winner is X")

    def test_inspectingDiag(self):
        self.assertEqual(ttt.inspecting_diag(self,board_list=[["X","O","O"],["O","X",6],["O",8,"X"]]),"Winner is X")

    def test_two_inspectingDiag(self):
        self.assertEqual(ttt.inspecting_diag(self,board_list=[["O","X","X"], [4,"O",6], [7, 8, "O"]]),"Winner is O")

    def test_inspectingReversDiag(self):
        self.assertEqual(ttt.inspecting_revers_diag(self,board_list=[[1,2,"O"],[4,"O",6],["O",7,8]]),"Winner is O")

    def test_draw_case(self):
        self.assertEqual(ttt.inspecting_revers_diag(self,board_list=[["O","X","O"],["X","O","O"],["X","O","X"]]),"There is no result yet")

    def test_check_for_board_game_on_False(self):
        self.assertFalse(ttt.check_for_board_game_on(self,"Winner is X" , "There is no result yet" , "There is no result yet" , "There is no result yet" ))

    def test_check_for_board_game_on_True(self):
        self.assertTrue(ttt.check_for_board_game_on(self,"There is no result yet" , "There is no result yet" , "There is no result yet", "There is no result yet"))

