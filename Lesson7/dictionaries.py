# # Dictianaries 

# band = {
#     "Vocals": "Plant",
#     "Guitar": "Page"
# }

# band2 = dict(Vocals="Plant1", Guitar="Page1")

# print(band)
# print(band2)

# print(type(band))
# print(len(band))
# print(type(band2))
# print(len(band2))


# # Access items in a dictionary 

# print(band ["Vocals"])
# print(band.get("Guitar"))

# #list all keys 

# print(band.keys())

# # list all values

# print(band.values())

# # list of key/value pairs as tupils 

# print(band.items())

# # verify if key exists 

# print("Guitar" in band)
# print("Drums" in band)


# # change values

# band["Vocals"] = "Coverdale"
# band.update({"Base": "JPJ"})

# print(band)

# # remove value

# print(band.pop("Base"))

# print(band)
# band["Drums"] = "Bonham"
# print(band)
# print(band.popitem())


# # delete and clear values 

# band["Drums"] = "Bonham"
# del band["Drums"]
# print(band)

# band2.clear()
# print(band2)

# del band2

# # copy dictionaries 

# band2 = band.copy()
# band2["Drums"] = "Bonham"
# print(band)
# print(band2)

# # or use the dict() constructor function

# band3 =dict(band)
# print(band3)

# # nested dictionaries 

# legionX111 = {
#     "primark": "Roboute Guilliman",
#     "chapter": "Ultramarines"
# }

# legionX1X = {
#     "primark": "Corvus Corax",
#     "chapter": "RavenGuard"
# }

# spacemarinelegions = {
#     "legionX111": legionX111,
#     "legionX1X": legionX1X
# }
# print(spacemarinelegions)
# print(spacemarinelegions["legionX111"]["chapter"])


# sets 

# nums = [1,2,3,4]
# nums2 = ((1,2,3,4))
# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums))

# no duplicztes allowed 
# nums = {1, 2, 2, 3, 4}

# print(nums)

# true is a dupe of 1 and false is a dupe of 0
# nums = {1, True, 2, False, 3, 4, 0}

# print(nums)

# # check if value is in a set  but you cannot refer to a value in a eliment in a set with an index position or a key

# print(2 in nums)

# # add an element to a set 

# nums.add(6)

# print(nums)

# # add elements from one set to another set 

# morenums = {5, 7, 8}
# nums.update(morenums)
# print(nums)

# you can use update with lists, tuples and dictionaries as well

# merge two sets to create a new set

# one = {1, 2, 3,}
# two = {4, 5, 6}

# newset = one.union(two)
# print(newset)

# one = {1, 2, 3,}
# two = {2, 3, 4, 5, 6}

# one.intersection_update(two)
# print(one)

# keep everything except the duplicates 
one = {1, 2, 3,}
two = {2, 3, 4, 5, 6}

one.symmetric_difference_update(two)
print(one)
