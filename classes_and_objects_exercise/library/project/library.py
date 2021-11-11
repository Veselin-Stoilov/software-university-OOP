class Library:
    def __init__(self):
        self.user_records = []  # [user1=obj, user2, user3...]
        self.books_available = {}  # {author1=str: [books=str], author2: [book1, Book2...]}
        self.rented_books = {}  # {User1=str: {book1=str: days=int}, User2: {book1: days, book2: days}}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user: object):
        if user in self.user_records:
            self.user_records.remove(user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id == user_id:

                if user.user_name == new_username:
                    return (
                        f"Please check again the provided username - it should be different "
                        f"than the username used so far!"
                    )
                old_name = user.user_name
                user.user_name = new_username
                for name in self.rented_books:

                    if name == old_name:

                        self.rented_books[new_username] = self.rented_books[old_name]
                        self.rented_books.pop(old_name)
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            return f"There is no user with id = {user_id}!"



