import book_manager
import borrow_manager
import file_storage

def wait_for_user():
    input("\nPress Enter to continue...")

def display_menu():
    print("\n" + "=" * 40)
    print("LIBRARY BOOK BORROWING SYSTEM")
    print("=" * 40)
    print("1. Add New Book")
    print("2. Display All Books")
    print("3. Display Available Books")
    print("4. Display Borrowed Books")
    print("5. Search Books by Category")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Update Book")
    print("9. Remove Book")
    print("10. Save Data")
    print("0. Exit")
    print("=" * 40)

def get_book_input():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author: ").strip()
    category = input("Enter Category: ").strip()
    return book_id, title, author, category

def get_member_input():
    print("\n--- Borrow Book ---")
    member_id = input("Enter Member ID: ").strip()
    member_name = input("Enter Member Name: ").strip()
    book_id = input("Enter Book ID to borrow: ").strip()
    return member_id, member_name, book_id

def get_update_input():
    print("\n--- Update Book ---")
    book_id = input("Enter Book ID to update: ").strip()
    title = input("Enter new Title (or press Enter to skip): ").strip()
    author = input("Enter new Author (or press Enter to skip): ").strip()
    category = input("Enter new Category (or press Enter to skip): ").strip()
    
    title = title if title else None
    author = author if author else None
    category = category if category else None
    
    return book_id, title, author, category

def main():
    books, borrowed_books, load_message = file_storage.load_data()
    print("Welcome to Library Book Borrowing System!")
    print(load_message)
    
    while True:
        display_menu()
        choice = input("\nEnter choice (0-10): ").strip()
        
        if choice == '1':
            book_id, title, author, category = get_book_input()
            success, message = book_manager.add_book(books, book_id, title, author, category)
            print(message)
            if success:
                file_storage.save_data(books, borrowed_books)
        
        elif choice == '2':
            result = book_manager.display_all_books(books)
            print(result)
            wait_for_user()
        
        elif choice == '3':
            result = book_manager.display_available_books(books)
            print(result)
            wait_for_user()
        
        elif choice == '4':
            result = borrow_manager.display_borrowed_books(books, borrowed_books)
            print(result)
            wait_for_user()
        
        elif choice == '5':
            category = input("Enter category to search: ").strip()
            if category:
                found_books = book_manager.display_books_by_category(books, category)
                if found_books:
                    print(f"\nBooks in category '{category}':")
                    print("-" * 40)
                    for book in found_books:
                        status = "Available" if book['available'] else "Borrowed"
                        print(f"ID: {book['id']}")
                        print(f"Title: {book['title']}")
                        print(f"Author: {book['author']}")
                        print(f"Status: {status}")
                        print("-" * 20)
                else:
                    print(f"No books found in category '{category}'")
                wait_for_user()
            else:
                print("Category is required!")
        
        elif choice == '6':
            member_id, member_name, book_id = get_member_input()
            success, message = borrow_manager.borrow_book(books, borrowed_books, book_id, member_id, member_name)
            print(message)
            if success:
                file_storage.save_data(books, borrowed_books)
        
        elif choice == '7':
            book_id = input("Enter Book ID to return: ").strip()
            success, message = borrow_manager.return_book(books, borrowed_books, book_id)
            print(message)
            if success:
                file_storage.save_data(books, borrowed_books)
        
        elif choice == '8':
            book_id, title, author, category = get_update_input()
            success, message = book_manager.update_book(books, book_id, title, author, category)
            print(message)
            if success:
                file_storage.save_data(books, borrowed_books)
        
        elif choice == '9':
            book_id = input("Enter Book ID to remove: ").strip()
            success, message = book_manager.remove_book(books, book_id)
            print(message)
            if success:
                file_storage.save_data(books, borrowed_books)
        
        elif choice == '10':
            success, message = file_storage.save_data(books, borrowed_books)
            print(message)
        
        elif choice == '0':
            success, message = file_storage.save_data(books, borrowed_books)
            print(message)
            print("Thank you for using the Library Book Borrowing System!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 0-10.")

if __name__ == "__main__":
    main()
