def number_increment(numbers):

    def increase():
        return [x + 1 for x in numbers]
        # TODO: Implement

    return increase()


print(number_increment([1, 2, 3, 4, 5]))
