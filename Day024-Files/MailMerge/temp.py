# def my_format(sentence, **names):
#     for key, val in names.items():
#         sentence = sentence.replace('{'+key+'}', val)
#     return sentence
#
#
# print(my_format("I'm Mr. {name}, look at me!", name="Meeseeks"))
# print(my_format("{a} {b} {c} {c}", a="wubba", b="lubba", c="dub"))
# print(my_format("The universe is bascally an animal", animal='Chicken'))
# print(my_format("The universe is bascally an animal"))


my_dict = {'a': 1, 'b': 2,
           'c': {'d': 3, 'e': 4,
                 'f': {'g': 5,
                       'h': {'i': 6}}}}


def all_keys(milon):
    for key, val in milon.items():
        if type(val) == dict:
            all_keys(val)
        else:
            print(f'{key} = {val}')


all_keys(my_dict)