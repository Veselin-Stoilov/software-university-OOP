class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        index = self.counter % len(self.sequence)
        value_to_return = self.sequence[index]
        self.counter += 1
        return value_to_return


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
