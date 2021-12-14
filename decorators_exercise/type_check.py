def type_check(param_type):
    def decorator(func):
        def wrapper(arg):
            same_types = isinstance(arg, param_type)
            if not same_types:
                return "Bad Type"
            result = func(arg)
            return result
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
