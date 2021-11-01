


# def three_vals(lst=None):
#     i = 0
#     while i < len(lst):
#         if i+3 < len(lst):
#             yield lst[i:i+3]
#             i += 3
#         elif i < len(lst):
#             yield lst[i:]
#             break
#
#
#
# test = three_vals([x for x in range(11)])
# try:
#     for i in range(6):
#         print(next(test))
# except StopIteration:
#     print('No more values')


