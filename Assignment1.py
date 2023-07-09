# 1)create a list of fruits by taking input from users
list = []
for i in range(1, 3):
    fruits = input("type the name of the fruits")
    list.append(fruits)
print(list)

# 2)combine two list
list1 = ["jenkins", "bsj", "qojva"]
list2 = ["45", "28", "01"]
list = []
for i in range(len(list1)):
    list.append(list1[i] + list2[i])
print(list)

# 3)add element to list
list1 = ["jenkins", "bsj", "qojva"]
for i in range(1, 3):
    fruits = input("type the name of the fruits")
    list1.append(fruits)
print(list1)

# 4)print only integer data from list
list1 = [1, "name", 4]
list2 = [x for x in list1 if type(x) == int or type(x) == float]
print(list2)

# 5
listOfStrings = ['is', 'are', 'at', 'why', 'what']
value = 'the'
if value not in listOfStrings:
    listOfStrings.append(value)

print(listOfStrings)
















