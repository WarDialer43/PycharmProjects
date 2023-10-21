# Global scope artifact available to everything in the file 
# global scope artifact can be accessed with in the function of the local scope
# but anything defined inside the local scope cannot access out side of that function



# name = "smith"

# Local scope define a function within the local scope 

# def greeting(firstname):
#     color = "blue"
#     print(color)
#     print(name)
#     print(firstname)

# greeting("john")




name = "smith"
count = 1
# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)

# We defines color inside of another local scope, then  
# we defined the function greeting inside of the another local scope
# the we called greeting and greeting prints colorand the name

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("smith")
another()