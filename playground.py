def add(*args):
    total = 0
    for item in args:
        total += item
    return total


print(add(1, 2, 3, 4, 2.4, 5, 7, 9, 6, -1.2))

def compute(n, **kwargs):
    if kwargs["multi"] != None:
        n *= kwargs["multi"]
    if kwargs["add"] != None:
        n += kwargs["add"]
    return n

print(compute(4, multi=5, add=3, sub=2))
