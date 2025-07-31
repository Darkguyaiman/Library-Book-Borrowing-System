def borrow_book(books, borrowed_books, book_id, member_id, member_name):
    if not member_id or not member_name or not book_id:
        return False, "All fields are required!"
    
    if book_id not in books:
        return False, "This book was not borrowed or does not exist"
    
    if not books[book_id]['available']:
        return False, "Book is not available!"
    
    books[book_id]['available'] = False
    borrowed_books[book_id] = {
        'member_id': member_id,
        'member_name': member_name
    }
    return True, "Book borrowed successfully"

def return_book(books, borrowed_books, book_id):
    if not book_id:
        return False, "Book ID is required!"
    
    if book_id not in books:
        return False, "This book was not borrowed or does not exist"
    
    if books[book_id]['available']:
        return False, "This book was not borrowed or does not exist"
    
    books[book_id]['available'] = True
    if book_id in borrowed_books:
        del borrowed_books[book_id]
    return True, "Book returned successfully"

def display_borrowed_books(books, borrowed_books):
    if not borrowed_books:
        return "No books are borrowed!"
    
    result = "\nBorrowed Books:\n" + "-" * 40 + "\n"
    for book_id, borrow_info in borrowed_books.items():
        book_info = books[book_id]
        result += f"Book ID: {book_id}\n"
        result += f"Title: {book_info['title']}\n"
        result += f"Borrowed by: {borrow_info['member_name']} (ID: {borrow_info['member_id']})\n"
        result += "-" * 20 + "\n"
    return result
