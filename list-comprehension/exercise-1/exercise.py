numbers_list1 = []
numbers_list2 = []
with open("file1.txt", "r") as file1:
    data = file1.readlines()
    numbers_list1 = [int(number) for number in data]

with open("file2.txt", "r") as file2:
    data = file2.readlines()
    numbers_list2 = [int(number) for number in data]

matched_number = [number for number in numbers_list1 if number in numbers_list2]
print(matched_number)