# define and then call functions 

# def hello_world():
#     print("HelloWorld!")

# hello_world()

# def sum(num1, num2):
#     print(num1 + num2)

# sum(1, 2)
# sum(100, 12)
# sum(3, 10)

# def sum(num1=0, num2=0):
#     if (type(num1) is not int or type(num2) is not int):
#         return 0
#     return num1 + num2

# total = sum()
# print(total)

# def multiple_items(*args):
#     print(args)
#     print(type(args))

def multi_named_item(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_item(first="ultra", last="marine")





