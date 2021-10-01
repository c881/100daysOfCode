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
