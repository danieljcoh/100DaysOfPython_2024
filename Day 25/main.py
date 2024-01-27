#
# import csv
# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         for word in row:
# #             if word.isdigit():
# #                 temperatures.append(int(word))
# #
# # print(temperatures)
#
#
#
import pandas
#
# t = []
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
# # average_temp = sum(temp_list) / len(temp_list)
# # print(round(average_temp, 2))
#
# # print(data["temp"].max())
#
#
# # print row
# # print(data[data.day == "Monday"])
#
#
# # we want to print out a dataframe row so we are going to look into a specific column and see if it equals something we're looking for
# # print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
#
# # F = (9/5)C + 32.
# monday_f = (9 / 5) * monday.temp[0] + 32
# print(monday_f)
#
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy"],
#     "scores": [50]
# }
#
# data1 = pandas.DataFrame(data_dict)
# print(data1)
#
#

# Squirrel Data Part
data = pandas.read_csv("squirrel_data.csv")

squirrel_color_list = data["Primary Fur Color"].to_list()
cinnamon_color = [i for i in squirrel_color_list if i == "Cinnamon"]
black_color = [i for i in squirrel_color_list if i == "Black"]
gray_color = [i for i in squirrel_color_list if i == "Gray"]
print(len(cinnamon_color))
print(len(black_color))
print(len(gray_color))

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [len(gray_color), len(cinnamon_color), len(black_color)]
}

squirrel_color_data = pandas.DataFrame(data_dict)
print(squirrel_color_data)

squirrel_color_data.to_csv("squirrel_color_data.csv")


print(type(data))


