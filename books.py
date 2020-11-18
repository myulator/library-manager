"""
Book collection manager.
Student: Michael Yu
Student ID: A00962260
Date: November 18, 2020
"""


def load_data():
    """
    Load all data from a text file into a data structure for use by the book manager.

    :precondition: there must be a text file in the current directory with the name 'Books UTF-16.txt'
    :postcondition: creates a data structure for the data in the file
    :return: a list containing dictionaries, with each dictionary representing the book info of one book

    >>> print(load_data())
    [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture',
    'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', 'Publisher':
    'Exeter', 'Shelf': '6', 'Category': 'Architecture'}, .... and so on, such that every book is in the list... ]
    """
    collection = []
    filename = 'Books UTF-16.txt'
    with open(filename, encoding='UTF-16') as file_object:
        keys_list = list(file_object.readline().strip().split('\t'))

        for line in file_object:
            book_info = list(line.strip().split('\t'))
            book_dict = {keys_list[i]: book_info[i] for i in range(6)}
            collection.append(book_dict)

    return collection


def menu(collection: list):
    """
    Ask user what they want to do.

    Print a menu to the screen that associates a number input with a function. Prompt the user for input.
    Proceed with the function pathway that matches user's input.

    :precondition: User must input either 1, 2, or 3.
    :postcondition: Execute the appropriate search, move, or quit function.
    :param collection: a list of dictionaries representing the book collection.
    :return: if user input is '2': return collection after book has been moved.
            if user input is '3': invalidate the main while loop condition and return it.

    --------------------------------------------
    Menu:
    1 = Search book collection
    2 = Change book location
    3 = Quit
    --------------------------------------------
    Please input a number to make a selection:
    """
    print('--------------------------------------------')
    print('Menu:')
    print('1 = Search book collection\n2 = Change book location\n3 = Quit')
    print('--------------------------------------------')

    menu_selection = int(input('Please input a number to make a selection: '))
    if menu_selection == 1:
        search(collection)
    elif menu_selection == 2:
        print('You are about to move a book. Let\'s begin by finding your book first.')
        move_book(collection)
        return collection
    elif menu_selection == 3:
        quit_requested = 1
        return quit_requested
    else:
        print('Error: That is not a valid input. Please enter a number from 1 to 3.')


def quit_books(collection: list):
    """
    Save the collection as a new file.

    Write all current information from collection data structure to a text file.

    :param collection: a list of dictionaries representing the book collection.
    :postcondition: always writes the current state of the collection into a new text file called programming.
    """
    filename = 'programming.txt'
    try:
        with open(filename, 'w', encoding='UTF-16') as file_object:
            # write the section headers into the file as the first line.
            file_object.write('Author\tTitle\tPublisher\tShelf\tCategory\tSubject\n')

            for book in collection:
                for key, value in book.items():
                    # write each detail of the book into the file, each followed with a tab.
                    file_object.write(value + '\t')
                file_object.write('\n')
        print('Collection has been saved successfully.')
    except UnicodeEncodeError:
        print('Encountered Unicode encoding error. Collection has not been saved properly.')
    finally:
        print('Exiting program.')


def move_book(collection: list):
    """
    Relocate a book in the collection.

    Call search function to find the book of interest. Ask user to identify which book they would like to move.
    Obtain user input for the new location from get_valid_locations.
    Change the location data of the book to the new location.

    :precondition: User must enter an integer between 1 and the largest number in the list of results.
    :postcondition: Change the location of the book by editing the value of the shelf key in its dictionary.
    :param collection: a list of dictionaries representing the book collection.
    :return: a list of dictionaries representing the book collection after modifying a book's location.
    """
    results_list = search(collection)
    # if there are no results the results list, go back to the main menu.
    if not results_list:
        return

    book_to_move = int(input('Please input the number of the book you wish to move: '))
    if book_to_move > len(results_list) or book_to_move <= 0:
        print('That result number is not in the list!')
        return

    new_location = get_valid_locations(collection)

    # locate the book in search_results and change the value of 'shelf' key to the new_location
    book_dict = results_list[book_to_move - 1]
    book_dict['Shelf'] = new_location
    print(f'The book has been successfully moved to {new_location}')


def get_valid_locations(collection: list):
    """
    Return a list of valid book locations

    :param collection: a list of dictionaries representing the book collection.
    :return: a list of all unique locations in the collection
    """
    unique_locations = []
    for number in range(1, 39):
        unique_locations.append(str(number))

    for book_dict in collection:
        if book_dict['Shelf'] not in unique_locations:
            unique_locations.append(book_dict['Shelf'])

    print(f'Here are the locations that you can move the book to: \n\tShelf numbers 1 to 38')
    for location in unique_locations[38:]:
        print(f'\t{location}')

    new_location = input('Please enter a number between 1 to 38 or the location name.')
    if new_location.strip() in unique_locations:
        return new_location
    else:
        print('That is not a valid location. Returning to the main menu.\n')


def search(collection: list):
    """
    Direct user to the desired search function.

    Prompt user to enter a number between 1 and 6 that represents the search filter choice of the user.
    Pass the collection and user input to search_results.
    Return the list of results obtained from search_results.

    :precondition: User must enter an integer between 1 and 6 inclusively.
    :postcondition: Execute the search using the selected search filter.
    :param collection: a list of dictionaries representing the book collection.
    :return: a list of the search results
    -------------------------------------
    Search for a book by:
    1 = Author
    2 = Title
    3 = Publisher
    4 = Shelf
    5 = Category
    6 = Subject
    -------------------------------------
    Please input a number to make a selection:
    >>>
    """
    print('--------------------------------------------')
    print('Search for a book by:')
    print('1 = Author\n2 = Title\n3 = Publisher\n4 = Shelf\n5 = Category\n6 = Subject')
    print('--------------------------------------------')
    search_input = int(input('Please input a number to make a selection:'))
    results = search_results(collection, search_input)
    return results


def search_results(collection: list, search_input: int):
    """
    Search for a book.

    This function accepts the search_input passed from search function to determine the desired search filter.
    E.g. A search_input of 3 would indicate that the user would like to search by publisher.

    :precondition: User must enter a non-empty string representing their search.
                    When searching by location/shelf, user must enter the exact number/name of the location.
    :postcondition: Print the number of results found and the enumerated list of search results, then return the list.
    :param collection: a list of dictionaries representing the book collection.
    :param search_input: an integer representing the user's desired search filter.
    :return: a list of dictionaries representing books that were pulled from the search.
    """
    filters = ['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject']
    results_list = []
    query = input(f'Searching by {filters[search_input - 1]} : ')
    if filters[search_input - 1] == 'Shelf':
        for book in collection:
            # This is a workaround for partial matches when searching by location.
            # E.g. If input is '1', books in shelf 12 will not appear in the search results.
            if query.strip().lower() == book[filters[search_input - 1]].lower():
                results_list.append(book)
    else:
        for book in collection:
            if query.strip().lower() in book[filters[search_input - 1]].lower():
                results_list.append(book)

    print(f'Your search returned {len(results_list)} result(s)\n')

    for book_dict in results_list:
        print(f'#{results_list.index(book_dict) + 1}')
        for key, value in book_dict.items():
            print(f'\t{key}: {value}')
        print('\n')

    return results_list


def main():
    """
    Drives the program.
    """
    collection = load_data()
    quit_program = 0
    print('Welcome to your book manager.')
    while quit_program != 'exit':
        query = menu(collection)
        if query == 1:
            quit_program = 'exit'
    quit_books(collection)


if __name__ == "__main__":
    main()
