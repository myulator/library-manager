from unittest import TestCase
from books import get_valid_locations
import io
from unittest.mock import patch, call


class TestGetValidLocations(TestCase):

    @patch('builtins.input', side_effect=['400'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_valid_locations_valid_shelf_number(self, mock_input, mock_stdout):
        argument = [{'Shelf': '400'}, {'Shelf': 'Toilet'}, {'Shelf': '12'}]
        expected_return = '400'
        actual_return = get_valid_locations(argument)
        self.assertEqual(expected_return, actual_return, "Location input is a valid shelf number.")

    @patch('builtins.input', side_effect=['Toilet'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_valid_locations_valid_name(self, mock_input, mock_stdout):
        argument = [{'Shelf': '13'}, {'Shelf': 'Toilet'}, {'Shelf': '12'}]
        expected_return = 'Toilet'
        actual_return = get_valid_locations(argument)
        self.assertEqual(expected_return, actual_return, "Location input is a valid location name.")

    # @patch('builtins.input', side_effect=['0'])
    # @patch('builtins.print')
    # def test_get_valid_locations_invalid_shelf_number(self, mock_input, mock_stdout):
    #     argument = [{'Shelf': 'Coffee'}, {'Shelf': 'Toilet'}, {'Shelf': 'Noguchi'}]
    #
    #     expected_print = 'That is not a valid location. Returning to the main menu.\n'
    #     print(expected_print)
    #     self.assertEqual(expected_print, mock_stdout.getvalue(), "Location input not a valid shelf number.")

    @patch('builtins.input', side_effect=['0'])
    @patch('builtins.print', new_callable=io.StringIO)
    def test_get_valid_locations_invalid_shelf_number(self, mock_input, mock_stdout):
        argument = [{'Shelf': 'Coffee'}, {'Shelf': 'Toilet'}, {'Shelf': 'Noguchi'}]
        get_valid_locations(argument)
        expected_print = 'That is not a valid location. Returning to the main menu.\n'
        mock_stdout.assert_called_with(expected_print)
