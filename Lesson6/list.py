# users = ['Alberto', 'Yoda', 'DeadPool', 'Hulk']

# data = ['Alberto', 53, True]

# emptylist = []

# # print("Alberto" in emptylist)

# # print(users[0])
# # print(users[-1])
# # print(users.index('Mike'))
# # print(len(emptylist))

# users.append('IronMan')
# print(users)

# users += ['StarLord', 'Rocket']
# print(users)

# users.extend(['Ultramarine', 'RavenGuard', 'AlphaLegion'])
# print(users)

# # users.extend(data)
# # print(users)

# users.insert(0, 'Alberto')
# users[11:11] = ['wolverene', 'SpiderMan']
# print(users)

# users[2:3] = ['Sid', 'Nick']
# print(users)


# users.remove('Sid')
# print(users)

# print(users.pop())
# print(users)

# del users[8]
# print(users)

# # del data
# data.clear()
# print(data)


# users[2:3] = ['alberto']
# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)

# nums = [12, 53, 33, 1, 92]
# nums.reverse()
# print(nums)

# # nums.sort(reverse=True)
# # print(nums)

# print(sorted(nums, reverse=True))
# print(nums)

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

# print(numscopy)
# mynums.sort()
# print(mynums)
# print(mycopy)

# print(type(nums))


# Tuples 

mytuple = tuple(('AlphaLegion', 'UltraMarine', 'RavenGuard'))

anothertuple = (1,2,2,2,2,3,4,5,6,)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Chris')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)


print(anothertuple.count(2))