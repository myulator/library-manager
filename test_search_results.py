from unittest import TestCase
from books import search_results
import io
from unittest.mock import patch


class TestSearchResults(TestCase):

    @patch('builtins.input', side_effect=['AB'])
    def test_search_results_author_upper_case_input(self, mock_input):
        argument1 = [{'Author': 'ABBA'}, {'Author': 'Cadabra'}, {'Author': 'BACK'}]
        argument2 = 1
        expected_return = [{'Author': 'ABBA'}, {'Author': 'Cadabra'}]
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Two books have an author with 'AB' in it.")

    @patch('builtins.input', side_effect=['lazy'])
    def test_search_results_title_lower_case_input(self, mock_input):
        argument1 = [{'Title': 'LAZY'}, {'Title': 'notLAzy'}, {'Title': 'lazY'}]
        argument2 = 2
        expected_return = [{'Title': 'LAZY'}, {'Title': 'notLAzy'}, {'Title': 'lazY'}]
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "All books have 'lazy' in the title with various cases.")

    @patch('builtins.input', side_effect=[''])
    def test_search_results_publisher_one(self, mock_input):
        argument1 = [{'Publisher': '1'}, {'Publisher': '2'}, {'Publisher': '3'}]
        argument2 = 3
        expected_return = [{'Publisher': '1'}, {'Publisher': '2'}, {'Publisher': '3'}]
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Empty input not allowed in precondition, but doing so should"
                                                         "return a list of every book in the collection.")

    @patch('builtins.input', side_effect=['3'])
    def test_search_results_shelf_number(self, mock_input):
        argument1 = [{'Shelf': 'Coffee'}, {'Shelf': '13'}, {'Shelf': '3'}]
        argument2 = 4
        expected_return = [{'Shelf': '3'}]
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Only one book with location that matches the input exactly.")

    @patch('builtins.input', side_effect=['nog'])
    def test_search_results_shelf_partial_name(self, mock_input):
        argument1 = [{'Shelf': 'Noguchi'}, {'Shelf': '13'}, {'Shelf': '3'}]
        argument2 = 4
        expected_return = []
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Input is not an exact match of location in the book.")

    @patch('builtins.input', side_effect=['sci'])
    def test_search_results_category_partial_search_order(self, mock_input):
        argument1 = [{'Category': 'political-sci'}, {'Category': 'political-ics'}, {'Category': 'political-cis'}]
        argument2 = 5
        expected_return = [{'Category': 'political-sci'}]
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Only one book has 'sci' input in the right order.")

    @patch('builtins.input', side_effect=['   trek      '])
    def test_search_results_subject_whitespace(self, mock_input):
        argument1 = [{'Subject': 'StarWars'}, {'Subject': 'StarTrek'}, {'Subject': 'Wilderness Trekking'}]
        argument2 = 6
        expected_return = [{'Subject': 'StarTrek'}, {'Subject': 'Wilderness Trekking'}]
        actual_return = search_results(argument1, argument2)
        self.assertEqual(expected_return, actual_return, "Whitespace leading and trailing the input.")
