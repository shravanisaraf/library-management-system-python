# Library Management System in Python

A simple library management system implemented in Python using Pandas for data handling.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the main.py file to start the application.

## Usage

The library management system uses an Excel file (`books.xlsx`) to store information about the library's books. Here's how to use the system:

1. **Search for Books**: Enter the title of a book to search for it in the library's collection. The system will display details about the book, including its author and whether it's currently borrowed.

2. **Add New Books**: To add a new book to the library, provide its title and author. The system will automatically update the Excel file to include the new book.

3. **Update Book Details**: If a book's author needs to be updated, enter its title and the new author's name. The system will update the corresponding entry in the Excel file.

4. **Borrow and Return Books**: Mark books as borrowed or returned by entering their titles. The system will update the Excel file accordingly to track the borrowing status of each book.

The Excel file acts as the persistent storage for the library's data, allowing users to manage the library's collection of books efficiently.


## Examples

![Library Management System](screenshots/library_management_system.png)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact me at sarafshrau@gmail.com .
