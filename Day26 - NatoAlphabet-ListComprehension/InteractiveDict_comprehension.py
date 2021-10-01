import random
names = ["Alex", 'Beth', 'Carolin', 'David', 'Ed', 'Fred']
students_score = {name:random.randint(1, 100) for name in names}
passed_students = {name:score for (name, score) in students_score.items() if score > 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word
# in the given sentence and calculates the number of letters in each word.
result = {word:len(word) for word in sentence[:-1].split(" ")}

# Write your code below:
print(result)
# -----------------------------------------------------------
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# You are going to use Dictionary Comprehension to create a dictionary called weather_f
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# Write your code 👇 below:

weather_f = {key:(value * 9/5 + 32) for (key, value) in weather_c.items()}

print(weather_f)

#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)