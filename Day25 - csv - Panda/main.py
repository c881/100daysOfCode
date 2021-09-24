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
# # PyArrow - to deal with parquet files
# import pyarrow
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# # print the average temperature
# print(data["temp"].mean())
# # print the highest temperature
# print(data["temp"].max())

# # print the raw with the highest temperature
# print(data[data.temp == data.temp.max()])
# print(data[data["temp"] == data["temp"].max()])
# data_temp_list = data["temp"].to_list()

# convert Monday temperature from C to F
# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * 9 / 5 + 32
# print(monday_temp_f)

# dataframe from scratch
# data_dict = {"students": ["Jack", "Amy", "Josh"],
#              "grades": [72, 82, 75]}
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
# print(sum(data_temp_list) / len(data_temp_list))

##squirl_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# size difference between csv and parquet - 70%
##squirl_data.to_parquet("2018_central.parquet")
##squirl_data_p = pandas.read_parquet("2018_central.parquet")
##print(squirl_data_p[1:5])

import pandas as pd
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(squirrel_data["Primary Fur Color"].value_counts())
squirrel_dict= {"Fur Colours":[x for x in squirrel_data["Primary Fur Color"].unique()[1:]],
                "Count":[]}
for value in squirrel_data["Primary Fur Color"].value_counts():
    squirrel_dict["Count"].append(value)
# squirrl_df = pd.DataFrame(squirrel_data["Primary Fur Color"].value_counts())   # pd.DataFrame(squirrel_dict)
squirrl_df = pd.DataFrame(squirrel_dict)
print(squirrl_df)
squirrl_df.to_csv("2018_fur.csv")

