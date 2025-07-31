import book_manager
import borrow_manager
import file_storage
import os

# Defining a specific file for testing to avoid interfering with the main application's data
TEST_DATA_FILE = "test_library_data.json"

def setup_initial_state(books_data=None, borrowed_data=None):
    """
    Sets up the initial state for a test by writing to the test data file.
    Ensures a clean slate for each test run if specific data is provided,
    otherwise loads current state.
    """
    if books_data is not None or borrowed_data is not None:
        if os.path.exists(TEST_DATA_FILE):
            os.remove(TEST_DATA_FILE)
        books = books_data if books_data is not None else {}
        borrowed_books = borrowed_data if borrowed_data is not None else {}
        file_storage.save_data(books, borrowed_books, filename=TEST_DATA_FILE)
    
    
    loaded_books, loaded_borrowed_books, _ = file_storage.load_data(filename=TEST_DATA_FILE)
    return loaded_books, loaded_borrowed_books

def get_current_state_from_file():
    books, borrowed_books, _ = file_storage.load_data(filename=TEST_DATA_FILE)
    return books, borrowed_books

def print_state(label, books, borrowed_books):
    print(f"\n--- {label} ---")
    print("Books:")
    if books:
        for book_id, info in books.items():
            print(f"  ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Category: {info['category']}, Available: {info['available']}")
    else:
        print("  No books.")
    print("Borrowed Books:")
    if borrowed_books:
        for book_id, info in borrowed_books.items():
            print(f"  Book ID: {book_id}, Member: {info['member_name']} (ID: {info['member_id']})")
    else:
        print("  No borrowed books.")
    print("-" * 30)

def wait_for_user_inspection():
    input("\nTest completed. You can now inspect 'test_library_data.json'. Press Enter to continue...")

# --- Test Cases ---

def test_add_book_scenario():
    """
    Test case 1: Adds a new book and verifies its presence.
    Example Input: Book ID 'B001', Title 'The Great Novel', Author 'Author A', Category 'Fiction'
    Expected Output: Book 'B001' is added and marked as available.
    """
    print("\n--- Running Test: Add Book Scenario ---")
    books, borrowed_books = setup_initial_state()
    print_state("State Before Test", books, borrowed_books)

    print("Attempting to add Book ID 'B001'")
    success, message = book_manager.add_book(books, "B001", "The Great Novel", "Author A", "Fiction")
    print(f"Operation Result: {message}")
    if success:
        file_storage.save_data(books, borrowed_books, filename=TEST_DATA_FILE)
    else:
        print("Add book failed, state not saved.")

    books_after, borrowed_books_after = get_current_state_from_file()
    print_state("State After Test", books_after, borrowed_books_after)
    wait_for_user_inspection()

def test_borrow_and_return_scenario():
    """
    Test case 2: Borrows a book and then returns it.
    Example Input (Borrow): Book ID 'B002', Member ID 'M001', Member Name 'Alice'
    Example Input (Return): Book ID 'B002'
    Expected Output: Book 'B002' is initially available, then borrowed and marked unavailable,
                     then returned and marked available again.
    """
    print("\n--- Running Test: Borrow and Return Scenario ---")
    initial_books = {
        "B002": {'title': 'Python Basics', 'author': 'Author B', 'category': 'Programming', 'available': True}
    }
    books, borrowed_books = setup_initial_state(initial_books)
    print_state("State Before Test", books, borrowed_books)

    print("\nAttempting to borrow Book ID 'B002' by Alice (M001)")
    success, message = borrow_manager.borrow_book(books, borrowed_books, "B002", "M001", "Alice")
    print(f"Borrow Result: {message}")
    if success:
        file_storage.save_data(books, borrowed_books, filename=TEST_DATA_FILE)
    else:
        print("Borrow book failed, state not saved.")

    books_current, borrowed_books_current = get_current_state_from_file()
    print_state("State After Borrow Attempt", books_current, borrowed_books_current)
    wait_for_user_inspection() 

    print("\nAttempting to return Book ID 'B002'")
    success, message = borrow_manager.return_book(books_current, borrowed_books_current, "B002")
    print(f"Return Result: {message}")
    if success:
        file_storage.save_data(books_current, borrowed_books_current, filename=TEST_DATA_FILE)
    else:
        print("Return book failed, state not saved.")
    
    books_after, borrowed_books_after = get_current_state_from_file()
    print_state("State After Return Attempt", books_after, borrowed_books_after)
    wait_for_user_inspection()

def test_update_and_remove_scenario():
    """
    Test case 3: Updates a book's details and then removes it.
    Example Input (Update): Book ID 'B003', new Title 'New Title', new Category 'New Category'
    Example Input (Remove): Book ID 'B003'
    Expected Output: Book 'B003' is initially with old details, then updated, then completely removed.
    """
    print("\n--- Running Test: Update and Remove Scenario ---")
    initial_books = {
        "B003": {'title': 'Old Title', 'author': 'Old Author', 'category': 'Old Category', 'available': True}
    }
    books, borrowed_books = setup_initial_state(initial_books)
    print_state("State Before Test", books, borrowed_books)

    print("\nAttempting to update Book ID 'B003' title and category")
    success, message = book_manager.update_book(books, "B003", "New Title", None, "New Category")
    print(f"Update Result: {message}")
    if success:
        file_storage.save_data(books, borrowed_books, filename=TEST_DATA_FILE)
    else:
        print("Update book failed, state not saved.")

    books_current, borrowed_books_current = get_current_state_from_file()
    print_state("State After Update Attempt", books_current, borrowed_books_current)
    wait_for_user_inspection()

    print("\nAttempting to remove Book ID 'B003'")
    success, message = book_manager.remove_book(books_current, "B003")
    print(f"Remove Result: {message}")
    if success:
        file_storage.save_data(books_current, borrowed_books_current, filename=TEST_DATA_FILE)
    else:
        print("Remove book failed, state not saved.")
    
    books_after, borrowed_books_after = get_current_state_from_file()
    print_state("State After Remove Attempt", books_after, borrowed_books_after)
    wait_for_user_inspection() 

def reset_test_data():
    """Deletes the test data file to reset the library state."""
    if os.path.exists(TEST_DATA_FILE):
        os.remove(TEST_DATA_FILE)
        print(f"\n'{TEST_DATA_FILE}' has been reset.")
    else:
        print(f"\n'{TEST_DATA_FILE}' does not exist. Nothing to reset.")

def display_test_menu():
    """Displays the menu for test options."""
    print("\n" + "=" * 40)
    print("LIBRARY SYSTEM TEST RUNNER")
    print("=" * 40)
    print("1. Run Add Book Scenario")
    print("2. Run Borrow and Return Scenario")
    print("3. Run Update and Remove Scenario")
    print("R. Reset Test Data")
    print("0. Exit Test Runner")
    print("=" * 40)

def main():
    """Main function for the interactive test runner."""
    print("Welcome to the Library System Test Runner!")
    
    while True:
        display_test_menu()
        choice = input("Enter your choice: ").strip().upper()

        if choice == '1':
            test_add_book_scenario()
        elif choice == '2':
            test_borrow_and_return_scenario()
        elif choice == '3':
            test_update_and_remove_scenario()
        elif choice == 'R':
            reset_test_data()
        elif choice == '0':
            print("Exiting Test Runner. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
