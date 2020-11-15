"""
Book collection manager.
Student: Michael Yu
Student ID: A00962260
Date: November 5, 2020
"""


def load_data():
    """
    Load all book data from the books.txt file

    :return: a tuple containing dictionaries, with each dictionary representing the book info of one book

    >>> print(load_data())
    [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture',
    'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', 'Publisher':
    'Exeter', 'Shelf': '6', 'Category': 'Architecture'}, .... and so on ... ]
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


def menu(collection):
    """
    Ask user what they want to do.

    Print a menu to the screen that associates a number input with a function. Prompt the user for input.
    Call the function that matches user's input.

    :precondition: User must input either 1, 2, or 3.
    :postcondition: Execute the appropriate search, move, or quit function.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: if user input is '2': return collection after book has been moved.
            if user input is '3': return the modified main while loop condition.

    --------------------------------------------
    Menu:
    1 = Search book collection
    2 = Change book location
    3 = Quit
    --------------------------------------------
    Please input a number to make a selection:
    """
    # Print a legend of input options
    print('--------------------------------------------')
    print('Menu:')
    print('1 = Search book collection\n2 = Change book location\n3 = Quit')
    print('--------------------------------------------')

    # Ask for input
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


def quit_books(collection):
    """
    Saves the file and exits the program.

    :param collection: a tuple of dictionaries representing the book collection.
    :postcondition: always writes the current state of the collection into a new text file called programming.
    """
    # Write current information from books() data structure to the books.txt file
    filename = 'programming.txt'
    try:
        with open(filename, 'w', encoding='UTF-16') as file_object:
            file_object.write('Author\tTitle\tPublisher\tShelf\tCategory\tSubject\n')
            for book in collection:
                for key, value in book.items():
                    file_object.write(value + '\t')
                file_object.write('\n')
        print('Collection has been saved successfully.')
    except UnicodeEncodeError:
        print('Encountered Unicode encoding error. Collection has not been saved properly.')
    finally:
        print('Exiting program.')


def move_book(collection):
    """
    Relocate a book in the collection.

    Call search function to find the book of interest. Ask user to identify which book they would like to move.
    Display a list of available locations from get_valid_locations.
    Prompt user to select the location they would like to move their selected book to.

    :precondition: User must enter an integer first, then a string representing the book's new location.
    :postcondition: Change the location of the book by editing the value of the shelf key in the dictionary.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a tuple of dictionaries representing the book collection after modifying a book's location.
    """
    # Call the search function and store the results
    results_list = search(collection)
    if not results_list:
        return
    book_to_move = int(input('Please input the number of the book you wish to move: '))

    # display all possible locations for the book to be moved
    new_location = get_valid_locations(collection)

    # locate the book (dictionary) in the search_results and change the value of 'shelf' key to the new_location
    book_dict = results_list[book_to_move - 1]
    book_dict['Shelf'] = new_location
    print(f'The book has been successfully moved to {new_location}')


def get_valid_locations(collection):
    """
    Return a list of valid book locations

    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of all unique locations in the collection
    """
    unique_locations = []
    for number in range(1, 39):
        unique_locations.append(str(number))

    for book_dict in collection:
        if book_dict['Shelf'] not in unique_locations:
            unique_locations.append(book_dict['Shelf'])

    # enumerate the results in the list and print them to the screen
    print(f'Here are the locations that you can move the book to: \n\tShelf numbers 1 to 38')
    for location in unique_locations[38:]:
        print(f'\t{location}')

    new_location = input('Please enter a number between 1 to 38 or the location name.')
    if new_location.strip() in unique_locations:
        return new_location
    else:
        print('That is not a valid location. Returning to the main menu.\n')


def search(collection):
    """
    Direct user to the desired search function.

    Accept an integer that represents the search filter choice of the user. Then call appropriate search function.

    :precondition: User must enter an integer.
    :postcondition: Execute the search using the selected search filter.
    :param collection: a tuple of dictionaries representing the book collection.
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


def search_results(collection, search_input):
    """
    Search for a book.

    This function accepts the search_input passed from search() to determine the desired search filter.
    E.g. A search_input of 3 would indicate that the user would like to search by publisher.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the author
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :param search_input: an integer representing the user's desired search filter
    :return: a list of dictionaries representing books that were pulled from the search
    """
    filters = ['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject']
    results_list = []
    query = input(f'Searching by {filters[search_input - 1]} : ')
    if filters[search_input - 1] == 'Shelf':
        for book in collection:
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
