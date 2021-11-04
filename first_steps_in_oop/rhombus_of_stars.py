size = int(input())


def spaces_count(size):
    spaces = size - 1
    return spaces


def single_line(spaces, stars):
    line = ''
    line += ' ' * (spaces - stars)
    line += '* ' * (stars + 1)
    return line


def triangle1(spaces):
    for stars in range(spaces):
        print(single_line(spaces, stars))

    for stars in range(spaces, -1, -1):
        print(single_line(spaces, stars))


triangle1(spaces_count(size))
