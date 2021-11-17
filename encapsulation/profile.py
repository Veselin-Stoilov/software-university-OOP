class Profile:
    _username_min_len = 5
    _username_max_len = 15
    _password_min_len = 8
    _password_min_digits = 1
    _password_min_upper = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __username_validation(self, username):
        error_message = f"The username must be between {self._username_min_len} " \
                        f"and {self._username_max_len} characters."
        if len(username) not in range(self._username_min_len, self._username_max_len + 1):
            raise ValueError(error_message)

    def __password_validation(self, password):
        error_message = f"The password must be {self._password_min_len} or more " \
                        f"characters with at least {self._password_min_digits} digit " \
                        f"and {self._password_min_upper} uppercase letter."
        if len(password) < self._password_min_len:
            raise ValueError(error_message)
        if len([x for x in password if x.isdigit()]) < self._password_min_digits:
            raise ValueError(error_message)
        if len([x for x in password if x.isupper()]) < self._password_min_upper:
            raise ValueError(error_message)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username_validation(new_username)
        self.__username = new_username

    @property
    def password(self):
        return "*" * len(self.__password)

    @password.setter
    def password(self, value):
        self.__password_validation(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" ' \
               f'and password: {self.password}'


import unittest

class Tests(unittest.TestCase):
    def test_invalid_password(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('My_username', 'My-password')
        self.assertEqual(str(ve.exception), "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('Too_long_username', 'Any')
        self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")

    def test_correct_profile(self):
        self.profile = Profile("Username", "Passw0rd")
        self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')

if __name__ == "__main__":
    unittest.main()


