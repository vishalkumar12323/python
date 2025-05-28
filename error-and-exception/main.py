# Python Errors: TypeError, IndexError, FileNotFoundError, IndentationError, NameError or VariableError

# def init():
#     print("hello world!")

# 1. FileNotFoundError
# try:
#     file = open("./text.txt", "r")
#     content = file.read()
#     print(content)
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError as file_err:
#     print(f"file error is {file_err}")
# except KeyError as key_err:
#     print(f"the key {key_err} does not exist.")
# else:
#     file = open("text.txt", 'w')
#     file.write("some string\n")
# finally:
#     file.close()



# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError as error:
#         print("Fruit pie")
#         # print(f"error is {error}")

# make_pie(2)



facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
        total_likes = 0
        for post in posts:
            try: 
                total_likes = total_likes + post['Likes']
            except:
                 pass
        return total_likes
        

print(count_likes(facebook_posts))
