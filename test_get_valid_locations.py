from unittest import TestCase
from books import get_valid_locations
import io
from unittest.mock import patch


class TestGetValidLocations(TestCase):

    @patch('builtins.input', side_effect=['400'])
    def test_get_valid_locations_valid_shelf_number(self, mock_input):
        argument = [{'Shelf': '400'}, {'Shelf': 'Toilet'}, {'Shelf': '12'}]
        expected_return = '400'
        actual_return = get_valid_locations(argument)
        self.assertEqual(expected_return, actual_return, "New location input is a valid shelf number.")

    @patch('builtins.input', side_effect=['Toilet'])
    def test_get_valid_locations_valid_name(self, mock_input):
        argument = [{'Shelf': '13'}, {'Shelf': 'Toilet'}, {'Shelf': '12'}]
        expected_return = 'Toilet'
        actual_return = get_valid_locations(argument)
        self.assertEqual(expected_return, actual_return, "New location input is a valid location name.")

    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_valid_locations_invalid_shelf_number(self, mock_stdout, mock_input):
        argument = [{'Shelf': 'Coffee'}, {'Shelf': 'Toilet'}, {'Shelf': 'Noguchi'}]
        get_valid_locations(argument)
        expected_print = 'Here are the locations that you can move the book to: \n\tShelf numbers 1 to 38\n\tCoffee\
\n\tToilet\n\tNoguchi\nThat is not a valid location. Returning to the main menu.\n\n'
        self.assertEqual(expected_print, mock_stdout.getvalue(), "New location input is not a valid shelf number.")

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_valid_locations_invalid_shelf_number(self, mock_stdout, mock_input):
        argument = [{'Shelf': 'Coffee'}, {'Shelf': 'Toilet'}, {'Shelf': 'Tree'}]
        get_valid_locations(argument)
        expected_print = 'Here are the locations that you can move the book to: \n\tShelf numbers 1 to 38\n\tCoffee\
\n\tToilet\n\tTree\nThat is not a valid location. Returning to the main menu.\n\n'
        self.assertEqual(expected_print, mock_stdout.getvalue(), "New location input is empty.")