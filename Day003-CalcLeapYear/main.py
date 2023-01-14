# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))

is_leap_year = False
if year % 4 == 0:
    is_leap_year = True
if is_leap_year and year % 100 == 0:
    is_leap_year = False
if not is_leap_year and year % 400 == 0:
    is_leap_year = True

if is_leap_year:
    print("Leap year.")
else:
    print('Not leap year.')
