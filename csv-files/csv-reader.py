# import csv
import pandas as pd

# with open("./weather-data.csv", 'r') as fd:
#     data = csv.reader(fd)
#     temp = []
#     for row_data in data:
#         if row_data[1] != 'temp':
#             temp.append(int(row_data[1]))

#     print(temp)

# print(pd.__version__)

data = pd.read_csv("./weather-data.csv")

# Get the average temp of the weather_list.
# weather_list = data["temp"].tolist()
# average_temp = sum(weather_list) / len(weather_list)
# print(average_temp)


# Get the one single row from data table
monday = data[data.day == "Monday"]
print(monday.temp)
# f_temp = (monday.temp[0] * 9/5) + 32
# print(f"{f_temp}f")