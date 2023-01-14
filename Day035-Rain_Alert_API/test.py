def return_int(num):
    num_a = 1
    while num_a < num:
        yield num_a
        num_a += 1

def find_lowest_missing_int(numbers):
    for number in return_int(100000):
        if number not in numbers:
            return number

print(find_lowest_missing_int([1,3,2,1,6]))
print(find_lowest_missing_int([-1,-3]))
print(find_lowest_missing_int([8,7,1,3,2,4,6]))
