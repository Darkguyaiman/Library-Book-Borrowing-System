def add_book(books, book_id, title, author, category):
    if not book_id or not title or not author or not category:
        return False, "All fields are required!"
    
    if book_id in books:
        return False, "Book ID already exists!"
    
    books[book_id] = {
        'title': title,
        'author': author,
        'category': category,
        'available': True
    }
    return True, "Book added successfully!"

def update_book(books, book_id, title=None, author=None, category=None):
    if book_id not in books:
        return False, "Book does not exist!"
    
    if title:
        books[book_id]['title'] = title
    if author:
        books[book_id]['author'] = author
    if category:
        books[book_id]['category'] = category
    
    return True, "Book updated successfully!"

def remove_book(books, book_id):
    if book_id not in books:
        return False, "Book does not exist!"
    
    if not books[book_id]['available']:
        return False, "Cannot remove borrowed book!"
    
    del books[book_id]
    return True, "Book removed successfully!"

def display_books_by_category(books, category):
    found_books = []
    for book_id, book_info in books.items():
        if book_info['category'].lower() == category.lower():
            book_data = book_info.copy()
            book_data['id'] = book_id
            found_books.append(book_data)
    return found_books

def display_all_books(books):
    if not books:
        return "No books in library!"
    
    result = "\nAll Books:\n" + "-" * 40 + "\n"
    for book_id, book_info in books.items():
        status = "Available" if book_info['available'] else "Borrowed"
        result += f"ID: {book_id}\n"
        result += f"Title: {book_info['title']}\n"
        result += f"Author: {book_info['author']}\n"
        result += f"Category: {book_info['category']}\n"
        result += f"Status: {status}\n"
        result += "-" * 20 + "\n"
    return result

def display_available_books(books):
    available = {k: v for k, v in books.items() if v['available']}
    
    if not available:
        return "No books available!"
    
    result = "\nAvailable Books:\n" + "-" * 40 + "\n"
    for book_id, book_info in available.items():
        result += f"ID: {book_id}\n"
        result += f"Title: {book_info['title']}\n"
        result += f"Author: {book_info['author']}\n"
        result += f"Category: {book_info['category']}\n"
        result += "-" * 20 + "\n"
    return result
