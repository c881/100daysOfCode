def add(*args):
    total = 0
    for item in args:
        total += item
    return total


print(add(1, 2, 3, 4, 2.4, 5, 7, 9, 6, -1.2))