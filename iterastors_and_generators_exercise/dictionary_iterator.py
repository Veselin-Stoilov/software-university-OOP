class dictionary_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.keys = list(self.iterable)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        value = self.iterable[self.keys[self.index]]
        self.index += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
