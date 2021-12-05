#  correct

class custom_range_iterator:
    def __init__(self, custom_range):
        self.custom_range = custom_range
        self.current_num = self.custom_range.start

    def __next__(self):
        if self.current_num > self.custom_range.end:
            raise StopIteration

        value_to_return = self.current_num
        self.current_num += 1
        return value_to_return


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iterator(self)


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

#  wrong

# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current_num = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_num > self.end:
#             raise StopIteration
#
#         value_to_return = self.current_num
#         self.current_num += 1
#         return value_to_return
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)

