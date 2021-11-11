class User:
    def __init__(self, user_id: int, user_name: str):
        self.user_id = user_id
        self.user_name = user_name
        self.books = []  # ???

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        for user in library.rented_books:
            for book in library.rented_books[user]:
                if book == book_name:
                    days_remaining = library.rented_books[user][book]
                    return (
                            f'The book "{book_name}" is already rented and will be available in '
                            f'{days_remaining} days!'
                    )
        for writer in library.books_available:
            if writer == author:
                if book_name in library.books_available[author]:
                    self.books.append(book_name)
                    library.rented_books[self.user_name] = {book_name: days_to_return}
                    library.books_available[author].remove(book_name)
                    return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.user_name} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        library.rented_books[self.user_name].pop(book_name)

    def info(self):
        result = ', '.join(self.books)
        return result

    def __str__(self):
        result = f"{self.user_id}, {self.user_name}, {self.books}"
        return result




