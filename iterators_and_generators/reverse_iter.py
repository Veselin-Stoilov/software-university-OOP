#  correct

class reverse_iter_iterator:
    def __init__(self, reverse_iter):
        self.reverse_iter = reverse_iter
        self.current_index = -1

    def __next__(self):
        if abs(self.current_index) > len(self.reverse_iter.iterable):
            raise StopIteration

        index_to_return = self.current_index
        self.current_index -= 1
        return self.reverse_iter.iterable[index_to_return]


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_index = -1

    def __iter__(self):
        return reverse_iter_iterator(self)


reversed_list = reverse_iter([1, 2, 3, 4, 5])
for item in reversed_list:
    print(item)

#  wrong

# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.current_index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if abs(self.current_index) > len(self.iterable):
#             raise StopIteration
#
#         index_to_return = self.current_index
#         self.current_index -= 1
#         return self.iterable[index_to_return]
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)







