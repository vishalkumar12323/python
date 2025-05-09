# simple list
# my_list = [{"name": "jem"}, 19, "Red"]
# print(my_list)
 
# another_list = list() # create a new empty list

# list comprehension
# numbers = [1, 2, 3 ,4, 5]
# new_list = [n+2 for n in numbers]

# name = "vishal"
# res = [latter.upper() for latter in name]

# new_name = "".join(res).title()
# print(new_name)


# check even numbers
# evens = [num for num in range(1, 21) if num % 2 == 0]
# print(evens)

# square numbers
# square = [num ** 2 for num in numbers]
# print(square)


# create a 3x3 matrix
# matrix = [[i for j in range(3)] for i in range(3)]
# print(matrix)


# pick short names
# names = ["bob", "casey", 'adam', "carlon", "rohit"]

# new_name = [name.upper() for name in names if len(name) >= 3]
# print(new_name)


numbers_list1 = []
numbers_list2 = []
with open("file1.txt", "r") as fd:
    data = fd.readline()
    numbers_list1.append(data)
    pass

print(numbers_list1)