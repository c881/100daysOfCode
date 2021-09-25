# # Review:
# # Create a function called greet().
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
#
# def greet(name):
#     print("Greeting")
#     print(f"Hello {name}")
#     print("See you later")
#
#
# greet("koby")
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"how is it like in {location}?")
#
# def greet_with_keyword(name, location):
#     print(f"Hello {name}")
#     print(f"how is it like in {location}?")
#

import art

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiplay
def mult(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2

# power
def pow(n1, n2):
    return n1 ** n2


operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
    '^': pow
}

num1 = int(input("what is your first number: "))
num2 = int(input("what is your next number: "))
for symbol in operations:
    print(symbol)
symbol = input("what is the operation you want to use: ")
if symbol in operations:
    print(f"{num1} {symbol} {num2} = {operations[symbol](num1, num2)}")

