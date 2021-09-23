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
# print the average temperature
print(data["temp"].mean())
# print the highest temperature
print(data["temp"].max())

# print the raw with the highest temperature
print(data[data.temp == data.temp.max()])
print(data[data["temp"] == data["temp"].max()])
# data_temp_list = data["temp"].to_list()

# convert Monday temperature from C to F
monday = data[data.day == "Monday"]
c_to_f = monday.temp * 9 / 5 + 32
print(c_to_f)

# print(sum(data_temp_list) / len(data_temp_list))