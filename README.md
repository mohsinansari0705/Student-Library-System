# Simple Student Library System

## Approach
This  simple project implements a simple student library system using two classes: `Library` and `Student`.

## Classes and Methods

### Library Class

**Constructor**: Initializes the list of books.

**Methods**:
- `listBooks()`: Lists all the books available in the library.
- `requestBook(bookName)`: Issues a book to a student and removes it from the list of available books.
- `returnBook(bookName)`: Accepts a returned book and adds it back to the list of available books.

### Student Class

**Methods**:
- `requestBook()`: Prompts the student to enter the name of the book they want to request.
- `returnBook()`: Prompts the student to enter the name of the book they want to return.

## Menu Options
The system provides a menu with the following options:

1. **List all the books**:
   - Prints the list of books available in the library using the `listBooks()` method from the `Library` class.

2. **Request a book**:
   - Takes the name of the book from the `requestBook()` method of the `Student` class.
   - Issues the book using the `requestBook()` method of the `Library` class.
   - Removes the book from the list of available books.

3. **Return the book**:
   - Takes the name of the book from the `returnBook()` method of the `Student` class.
   - Adds the book back to the list of available books using the `returnBook()` method of the `Library` class.

4. **Exit**:
   - Prints an exit message and terminates the program.

## Usage
To use the Simple Student Library System, follow these steps:

1. Clone the repository.
2. Run the main script.
3. Follow the on-screen menu to interact with the library system.