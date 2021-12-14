class StoreResults(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        with open("results.txt", "a") as file:
            file.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")
        print(f"Function '{self.func.__name__}' was called. Result: {result}\n")
        return


@StoreResults
def add(a, b):
    return a + b


@StoreResults
def mult(a, b):
    return a * b


add(2, 2)
add(9, 7)
mult(6, 4)
mult(3, 12)
