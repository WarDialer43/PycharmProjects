# String data type 

# litteral assigment of values 

first = "Alberto"
last = "Sbicca"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# another way to do the same thing is with a 'Constructor Function'

# pizza = str("Pepperoni")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Adding  two Strings together to form one String 'Concatanetion'

# fullname = first + " " + last

# print(fullname)

# fullname += "!"

# print(fullname)


# Converting a number to a String is called 'Casting'

# decade = str(1968)
# print(type(decade))
# print(decade)

# statement = "I like common sense from the " + decade + "s."
# print(statement)

# Statements with multiple lines 

# multiline = '''
# Hi Whats up ?                                      

# Just checking in !                                                         

#                                             All Good ?

# '''


# print(multiline)


# #Escaping special characters 

# sentence = 'I\'m looking for a new gig !\tbut\n\nlocated\'s in\\London!'

# print(sentence)

# String Methods are Functions that are called on the String Class 

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("All Good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                                    "
# multiline  = "                          " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


# # Build a menu 

# title = "menu".upper()
# print(title.center (20, "="))
# print("Coffe".ljust(16, ".") + "£1".rjust(4))
# print("Toast".ljust(18, ".") + "£1.50p".rjust(4))
# print("2x Eggs".ljust(18, ".") + "£1.20p".rjust(4))
# print("2x Bacon".ljust(18, ".") + "£2.50p".rjust(4))

# print(" ")

# String Index Values 

# print(first[0])
# print(first[1])
# print(first[-1])
# print(first[1:])

# # Methods that return Boolean Data
# print(first.startswith("A"))
# print(first.endswith("w"))

# Boolean data types 

# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# # Interger(int) types

# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# Float types 

gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(gpa, float))




