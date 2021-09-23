# with open("./weather_data.csv", "r") as weather_file:
#     data = [d1.split(',') for d1 in [d.strip() for d in weather_file.readlines()]]
#     temperature = [int(item[1]) for item in data[1:]]
#
#     # for item in data:
#     #     print(item)
#     print(temperature)
#
# import csv
# with open("./weather_data.csv", "r") as weather_file:
#     data = csv.reader(weather_file)
#     temperature = [int(item[1]) if item[1].isnumeric() else 0 for item in data]
#     temperature = temperature[1:]
#     # for row in data:
#         # print(row)
#     print(temperature)
#
#
#

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)