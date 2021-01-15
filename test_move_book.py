from unittest import TestCase
import books
import io
from unittest.mock import patch


class TestMoveBook(TestCase):

    @patch('books.search', side_effect=[[]])
    def test_move_book_empty_search_list(self, mock_search):
        argument = [{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]
        actual_return = books.move_book(argument)
        expected_return = None
        self.assertEqual(expected_return, actual_return, "Search results list is empty.")

    @patch('books.search', side_effect=[[{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]])
    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_input_not_in_results_list(self, mock_stdout, mock_input, mock_search):
        argument = [{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]
        actual_return = books.move_book(argument)
        expected_return = None
        expected_print = 'That result number is not in the list!\n'
        self.assertEqual(expected_return, actual_return, "User input is larger than the length of results list.")
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('books.search', side_effect=[[{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]])
    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_input_is_zero(self, mock_stdout, mock_input, mock_search):
        argument = [{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]
        actual_return = books.move_book(argument)
        expected_return = None
        expected_print = 'That result number is not in the list!\n'
        self.assertEqual(expected_return, actual_return, "User input is 0.")
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('books.get_valid_locations', side_effect=['Desk'])
    @patch('books.search', side_effect=[[{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]])
    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_valid_input(self, mock_stdout, mock_input, mock_search, mock_new_location):
        argument = [{'Shelf': '30'}, {'Shelf': 'Desk'}, {'Shelf': '12'}]
        actual_return = books.move_book(argument)
        expected_return = None
        expected_print = 'The book has been successfully moved to Desk\n'
        self.assertEqual(expected_return, actual_return, "User input is valid.")
        self.assertEqual(expected_print, mock_stdout.getvalue())

