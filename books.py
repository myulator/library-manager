"""
Book collection manager.
Student: Michael Yu
Student ID: A00962260
Date: November 5, 2020
"""
# Possible Book Locations

# shelf = []
# bedroom = []
# quilting_room = []
# coffee_table = []


def books():
    """
    Create a dictionary data structure that stores information from a text file
    """
    collection = load_data()
    return collection

    pass


def load_data():
    """
    Load all book data from the books.txt file

    :return: a tuple containing dictionaries, with each dictionary representing the book info of one book

    >>> print(load_data())
    [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture'},
    {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', 'Publisher': 'Exeter', 'Shelf': '6',
    'Category': 'Architecture'}, .... and so on ... ]
    """
    collection = []
    filename = 'Books UTF-16.txt'
    with open(filename, encoding='UTF-16') as file_object:
        keys_list = list(file_object.readline().split('\t'))

        for line in file_object:
            book_info = list(line.split('\t'))
            book_dict = {keys_list[i]: book_info[i] for i in range(5)}
            collection.append(book_dict)
    tuple(collection)
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
    Please make a selection:
    1 = Search book collection
    2 = Change book location
    3 = Quit
    --------------------------------------------
    Please input a number and press enter to make a selection:
    """
    # Print a legend of input options
    print('--------------------------------------------')
    print('Menu:')
    print('1 = Search book collection\n2 = Change book location\n3 = Quit')
    print('--------------------------------------------')

    # Ask for input
    menu_selection = input('Please input a number to make a selection:')
    if menu_selection == 1:
        search(collection)
    elif menu_selection == 2:
        move_book(collection)
        return collection
    elif menu_selection == 3:
        quit_requested = 1
        return quit_requested

    pass


def quit_books(collection):
    """
    Saves the file and exits the program.

    :param collection: a tuple of dictionaries representing the book collection.
    :postcondition: always writes the current state of the collection into a new text file called programming.
    """
    # Write current information from books() data structure to the books.txt file

    filename = 'programming.txt'
    with open(filename, 'w') as file_object:
        for line in collection:
            file_object.write(line)
    pass


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
    search_results = search(collection)
    book_to_move = int(input('Please input the result number that corresponds to the book you wish to move: '))

    # display all possible locations for the book to be moved
    get_valid_locations(collection)
    new_location = input('Please input the location you wish to move the book to: ')

    # locate the book (dictionary) in the search_results and change the value of 'shelf' key to the new_location
    book_dict = search_results[(book_to_move) - 1]
    book_dict['shelf'] = new_location

    return collection
    pass


def get_valid_locations(collection):
    """
    Return a list of valid book locations

    :param collection: a tuple of dictionaries representing the book collection.
    """
    locations = []
    # for loop over the collection and append unique locations to the location list
    # enumerate the results in the list and print them to the screen
    pass


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
    Please input a number to make a selection:
    >>>
    """

    search_input = input('Please input a number to make a selection:')
    if search_input == 1:
        search_results = search_author(collection)
    if search_input == 2:
        search_results = search_title(collection)
        # and so on...

    return search_results
    pass


def search_title(collection):
    """
    Search for a book by its title.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the book title
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of the search results
    """
    pass


def search_author(collection):
    """
    Search for a book by its author.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the author
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of the search results
    """
    pass


def search_publisher(collection):
    """
    Search for a book by its publisher.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the publisher
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of the search results
    """
    pass


def search_shelf(collection):
    """
    Search for a book by its shelf.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the shelf
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of the search results
    """
    pass


def search_category(collection):
    """
    Search for a book by its category.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the category
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of the search results
    """
    pass


def search_subject(collection):
    """
    Search for a book by its subject.

    :algorithm:
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the subject
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    5. return the list

    :precondition: User must enter a string representing their search.
    :postcondition: Print an enumerated list of search results to the screen, then return the list.
    :param collection: a tuple of dictionaries representing the book collection.
    :return: a list of the search results
    """
    pass


def main():
    """
    Drives the program.
    """
    collection = books()
    quit_requested = 0
    while quit_requested != 1:
        menu(collection)
    if quit_requested == 1:
        quit_books(collection)

if __name__ == "__main__":
    main()
