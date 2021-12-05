#  correct

class VowelsIterator:
    all_vowels = {"a", "e", "i", "o", "u", "y", "w"}

    def __init__(self, vowels):
        self.vowels = vowels
        self.current_index = 0

    def __next__(self):
        while True:
            if self.current_index >= len(self.vowels.string):
                raise StopIteration
            letter = self.vowels.string[self.current_index]
            self.current_index += 1
            if letter.lower() in self.all_vowels:
                return letter
            continue


class vowels:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return VowelsIterator(self)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

#  wrong

# class vowels:
#     all_vowels = {"a", "e", "i", "o", "u", "y", "w"}
#
#     def __init__(self, string):
#         self.string = string
#         self.current_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             if self.current_index >= len(self.string):
#                 raise StopIteration
#             letter = self.string[self.current_index]
#             self.current_index += 1
#             if letter.lower() in self.all_vowels:
#                 return letter
#             continue
