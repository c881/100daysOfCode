numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
squared_numbers = [num * num for num in numbers]


#Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
#Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 == 0]


#Write your code 👆 above:

print(result)

#You are going to create a list called result which contains the numbers that are common in both files.
with open("file1.txt","r") as in_file_1, open("file2.txt", "r") as in_file_2:
    lines1 = in_file_1.readlines()
    lines2 = in_file_2.readlines()
    result = [int(num) for num in lines1 if num in lines2]
    print(result)
