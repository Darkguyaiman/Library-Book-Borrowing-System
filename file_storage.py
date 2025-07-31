import json
import os

def save_data(books, borrowed_books, filename="library_data.json"):
    try:
        data = {'books': books, 'borrowed_books': borrowed_books}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        return True, "Data saved successfully!"
    except:
        return False, "Error saving data!"

def load_data(filename="library_data.json"):
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                books = data.get('books', {})
                borrowed_books = data.get('borrowed_books', {})
                return books, borrowed_books, "Data loaded successfully"
        else:
            return {}, {}, "No existing data file found. Starting with empty library."
    except:
        return {}, {}, "Error loading data. Starting with empty library."
