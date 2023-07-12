#Individual Assignment by Siddhartha Malhotra

#1. Accept numbers from a user
number = input("Type a number")
print(number)

#4. Print First 10 natural numbers using while loop
idx = 1 #zero is not a natural number hence idx is 1
while idx < 11:
    print(idx)
    idx = idx + 1

#5. Print the following pattern
 #1
 #1 2
 #1 2 3
 #1 2 3 4
 #1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()


#6. Calculate the sum of all numbers from 1 to a given number
t = int(input("choose a number"))
total = 0

for i in range(1, t+1):
    total += i

print(total)

#7. Write a program to print multiplication table of a given number
given_number = int(input("choose any number"))
for i in range(1, 15):
    product = given_number * i
    print(product)

#8. Display numbers from a list using loop
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(list1)):
    print(list1[i])

#9. Count the total number of digits in a number
num1 = (input('enter a number: '))
length1 = print(len(num1))

#10. Print the sum of the current number and the previous number
c = int(input('enter a number: '))
p = c-1
t = c + p
print(t)

#Reverse a list in Python
list1 = [1,2,3,4,5,6,7,8,9]
print(list1.reverse())

#Concatenate two lists index-wise
List1 = ["M", "na", "i", "Ke"]
List2 = ["y", "me", "s", "lly"]
new_list = []
for elements in range(len(List1 and List2)):
    new_list.append(List1[elements] + List2[elements])
print(new_list)
#o/p---> ['My', 'name', 'is', 'Kelly']

#--> Turn every item of a list into its square
list_num = [1,2,3,4,5,6,7,8,9]
num_list_square = []
for i in range(len(list_num)):
    num_list_square.append(list_num[i]**2)
print(num_list_square)

#--> Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
updated_list = []
for x in range(len(list1)):
    for y in range(len(list2)):
        updated_list.append(list1[x] + list2[y])
print(updated_list)
#o/p---> ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

#--> Iterate both lists simultaneously
lst1 = [10, 20, 30, 40]
lst2 = [100, 200, 300, 400]

for i in range(len(lst1)):
    first = lst1[i]
    second = lst2[i]
    print(first, second)

#--> Remove empty strings from the list of strings
list_one = ["Mike", "", "Emma", "Kelly", "", "Brad"]
i = 0
while i < len(list_one):
    if list_one[i] == "":
        list_one.remove(list_one[i])
    else:
        i += 1

print(list_one)
