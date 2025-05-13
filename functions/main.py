
#@ *args positional arguments
def add(*nums):
    total = 0
    for n in nums:
        total = total + n
    return total

# print(add(2, 3, 1, 4, 5))

#@ **args keword arguments

def calculate(**kwargs):
    info:list = kwargs["info"]
    print(info[0])

calculate(greet="hello", info=['vishal', 18])