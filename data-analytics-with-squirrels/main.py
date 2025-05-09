import pandas as pd

squirrel_data = pd.read_csv('./Squirrel-Census-Data.csv')

# Method 1.
# squirrel_colors_list = squirrel_data["Primary Fur Color"].to_list()
# gray = []
# cinnamon = []
# black = []
# for color in squirrel_colors_list:
#     if color == "Gray":
#         gray.append(color)
#     elif color == "Black":
#         black.append(color)
#     elif color == "Cinnamon":
#         cinnamon.append(color)

# new_data = {
#     "Fur Color": ['gray', 'black', 'cinnamon'],
#     "Count": []
# }

# pd.DataFrame(new_data).to_csv("./color-count.csv")


# Method 2.
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ['gray', 'black', 'red'],
    "Count": [gray_count, black_count, red_count]
}
pd.DataFrame(data_dict).to_csv("./color-count.csv")
