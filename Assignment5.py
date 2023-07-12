# Assignment
# ------------
# WAP to get the value from the dictionary for the given key
dict1 = {"apples": 1, "oranges": 2, "bananas": 3, "grapes": 4}
key = "apples"  # key is the name of the key
value = dict1.get(key)  # get() function is used to get the value from the key declaration from dict1
print(value)

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x,
# x*x). Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
number_dict = {}
for i in range(0, 5):
    number_dict[i] = i * i
print(number_dict)

# Write a Python script to merge two Python dictionaries.
dictionary1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dictionary2 = {5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

merged_dict = {**dictionary1, **dictionary2}
print(merged_dict)

# Write a Python program to values all the items in a dictionary.
dict_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(dict1.values())

# Write a Python program to check if a dictionary is empty or not.
dict_3 = {1: 1, 2: 4, 3: 4}
if dict_3 == {}:
    print("The dictionary is empty")
else:
    print(dict_3, "The dictionary is not empty")

# if it is filled don't add data or else add key value pair
dict4 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dict5 = {}

if dict5 == dict4:
    print("The dictionary has data")  # if statement is empty then print statement is printed, not adding any data
elif dict5 == {}:
    dict5["2"] = 4  # else if statement adding key value pair if dict5 is empty

print(dict5)

# Write a Python program to print all distinct values in a dictionary.
# Expected Output : Unique Values: {# 'S005', 'S002', 'S007', 'S001', 'S009'}

data_dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                   {"VIII": "S007"}]

distinct_values = set()
for i in data_dictionary:
    for j in i.values():
        distinct_values.add(j)
print(distinct_values)