# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# temp_list = data["temp"].to_list()
#
# average = sum(temp_list) / len(temp_list)
# print(round(average))
#
# print(data["temp"].max())

# print(data[data["temp"] == data["temp"].max()])


# monday = data[data.day == "Monday"]
# celcius = monday.temp
# farenheit = (celcius * 9/5) + 32
# print(farenheit)

# grouped_data = data.groupby("Primary Fur Color")['Primary Fur Color'].count().count

grouped_data = data.groupby("Primary Fur Color")['Primary Fur Color'].count().reset_index(name="Count").to_csv("squirrel_count.csv")

print(grouped_data)




