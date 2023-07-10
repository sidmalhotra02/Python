#List
#------

#Write a Python program to create a list.
create_list = [1,2,3,4,5]
print(create_list)

#Write a Python program to add an element to a list.
new_list = [1,2,3,4,5]
new_list.append(6)
print(new_list)

#Write a Python program to remove an element from a list.
lst1 = [1,2,3,4,5]
lst1.remove(2)
print(lst1)

#Write a Python program to sort a list.
list_s = [2,3,1,4,6,8,9]
list_s.sort()
print(list_s)

#Write a Python program to reverse a list.
list_r = [1,2,3,4,5]
list_r.reverse()
print(list_r)

#Write a Python program to find the maximum element in a list.
number = [11212,22,2233,433,544,63,565,2902]
print(max(number))

#Write a Python program to find the minimum element in a list.
number_m = [11212,22,2233,433,544,63,565,2902]
print(min(number))

#Write a Python program to find the sum of all elements in a list.
number_s = [1,2,3,4,5,6,7,8]
print(sum(number_s))

##Write a Python program to find the average of all elements in a list.
number_a = [1,2,3,4,5,6,7,8]
print(sum(number_a) / len(number_a))

#Write a function to find the maximum and minimum values in a list.
number_mm = [11212,22,2233,433,544,63,565,2902]
print(min(number_mm))
print(max(number_mm))

#Write a function to reverse the order of a list.
list_r2 = [1,2,3,4,5]
list_r2.reverse()
print(list_r2)

#Write a function to sort a list in ascending or descending order.
#ascending order
list_asc = [5,4,3,2,1]
list_asc.sort()
print(list_asc)
#descending order
list_desc = [1,2,3,4,5]
list_desc.sort(reverse=True)
print(list_desc)

#Write a function to remove duplicates from a list.
duplicates_list = [1,1,1,2,2,3,4,5,6,7,8,8,8,9]
not_duplicates_list = []
for i, x in enumerate(duplicates_list):
    if x not in not_duplicates_list:
        not_duplicates_list.append(x)
print(not_duplicates_list)

#Write a function to find the index of a given element in a list.
un_indexed_list = [1,2,3,4,5,6,7]
indexed_list = []
for i in range(len(un_indexed_list)):
    if un_indexed_list[i] == 2:
        indexed_list.append(i)
print(indexed_list)

#Tuple
#-------
#Write a Python program to create a tuple.
demo_tuple = (1,2,3,4)
print(demo_tuple)

#Write a Python program to add an element to a tuple.
tuple_1 = (1, 2, 3, 4, 5, 6, 7)
tuple_2 = tuple_1 + (8, 9, 10)
print(tuple_2)

#Write a Python program to remove an element from a tuple.
tuple_3 = (1, 2, 3, 4, 5) #Using list conversion
tuple_list = list(tuple_3)
tuple_list.remove(2)
new_tuple = tuple(tuple_list)
print(new_tuple)

#Write a Python program to sort a tuple.
tuple_s = (2,3,1,4,6,8,9)
new_tuple_s = tuple(sorted(tuple_s))
print(new_tuple_s)

#Write a Python program to reverse a tuple.
tuple_r = (1,2,3,4,5)
new_tuple_r = tuple(reversed(tuple_r))
print(new_tuple_r)

#Write a Python program to find the maximum element in a tuple.
tuple_m = (11212,22,2233,4)
print(max(tuple_m))

#Write a Python program to find the minimum element in a tuple.
tuple_m = (11212,22,2233,4)
print(min(tuple_m))

#Write a Python program to find the sum of all elements in a tuple.
tuple_s = (1,2,3,4,5,6,7,8)
print(sum(tuple_s))

#Write a Python program to find the average of all elements in a tuple.
tuple_a = (1,2,3,4,5,6,7,8)
print(sum(tuple_a) / len(tuple_a))

#Sets
#
#Write a Python program to create a set.
set_1 = {1,2,3,4,5}
print(set_1)

#Write a Python program to add an element to a set.
set_2 = {1,2,3,4,5}
set_2.add(6)
print(set_2)

#Write a Python program to remove an element from a set.
set_3 = {1,2,3,4,5}
set_3.remove(2)
print(set_3)

#Write a Python program to find the union of two sets.
set_4 = {1,2,3,4,5}
set_5 = {6,7,8,9,10}
print(set_4 | set_5)

#Write a Python program to find the intersection of two sets.
set_6 = {1,2,3,4,5,6}
set_7 = {5,6,7,8,9,10}
print(set_6 & set_7)

#Write a Python program to find the difference of two sets.
set_8 = {1,2,3,4,5,6}
set_9 = {5,6,7,8,9,10}
print(set_8 - set_9)

#Write a Python program to find the symmetric difference of two sets.
set_10 = {1,2,3,4,5,6,7,8,9,10}
set_11 = {5,6,7,8,9,10}
print(set_10 ^ set_11)

#Write a Python program to check if an element is present in a set.
set_12 = {1,2,3,4,5,6,7}
print(1 in set_12)
print(8 in set_12)

#Write a Python program to print all elements of a set.
set_13 = {1,2,3,4,5,6,7}
print(set_13)

