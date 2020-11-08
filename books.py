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
    Return all book data from the books.txt file

    :return: a tuple containing dictionaries, with each dictionary representing the book info of one book

    >>> load_data()

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
    # pass
    filename = 'programming.txt'
    with open(filename, 'w') as file_object:
        for line in collection:
            file_object.write(line)
    pass


def move_book(book, new_location):
    """
    Relocate a book in the collection.

    Call search function to find the book of interest. Ask user to identify which book they would like to move.

    Return a list of the collection from get_valid_locations
    Ask which book would I like to move out of the collection


    """
    pass


def get_valid_locations():
    """
    loop through collection, add collection to set
    """
    pass


def search(collection):
    """
    Direct user to the desired search function.

    Accept an integer that represents the search filter choice of the user. Then call appropriate search function.

    :param collection: a tuple of dictionaries representing the book collection.

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
        search_author(collection)
    if search_input == 2:
        search_title(collection)
        # and so on...
    pass


def search_title(collection):
    """
    Search for a book by its title.

    :param collection: a tuple of dictionaries representing the book collection.


    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the book title
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    """


    pass


def search_author(collection):
    """
    Search for a book by its author.

    :param collection: a tuple of dictionaries representing the book collection.
    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the author
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    """
    pass


def search_publisher(collection):
    """
    Search for a book by its publisher.

    :param collection: a tuple of dictionaries representing the book collection.

    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the publisher
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    """
    pass


def search_shelf(collection):
    """
    Search for a book by its shelf.

    :param collection: a tuple of dictionaries representing the book collection.

    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the shelf
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    """
    pass

def search_category(collection):
    """
    Search for a book by its category.

    :param collection: a tuple of dictionaries representing the book collection.

    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the category
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
    """
    pass


def search_subject(collection):
    """
    Search for a book by its subject.

    :param collection: a tuple of dictionaries representing the book collection.

    1. what are you searching for (store the input)
    2. loop through each tuple of books, check the value associated with the subject
    3. make a temporary list of addresses of the books in memory
    4. use enumerate function to print out the contents of each dictionary (this will show all search results)
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

if __name__ == "__main__":
    main()
