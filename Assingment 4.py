# Input and output operations
# ---------------------------

# Exercise 1: Accept numbers from a user
input_number = input("Enter a number: ")

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name*Is*James”
print("Name", "Is", "James")

# Exercise 3: Convert Decimal number to octal using print() output formatting
input_number1 = int(input("Enter a number: "))
print(oct(input_number1))

# Exercise 4: Display float number with 2 decimal places using print()
input_number2 = float(input("Enter a number: "))
print(float(input_number2))

# Exercise 5: Accept a list of 5 float numbers as an input from the user
input_list = []
for i in range(5):
    input_list.append(float(input("Enter a number: ")))
print(input_list)
# Exercise 6: Write all content of a given file into a new file by skipping line number 5
write_file = open("file.txt", "w")
line_number = 0

for i in range(5):
    line_number += 1
    if line_number != 5:
        write_file.write(input("Enter a number: "))

write_file.close()

# Exercise 7: Accept any three string from one input() call
string2 = ""
for i in range(3):
    string2 = input("Enter a string: ")
    print(string2)

# Exercise 8: Format variables using a string.format() method.
formatted_string = "Hello, {0}!"
print(formatted_string.format("James"))

# Exercise 9: Check file is empty or not
check_file = open("file.txt", "r")
if check_file.read() == "":
    print("File is empty")

# Exercise 10: Read line number 4 from the following file
check_file = open("file.txt", "r")
line_number = check_file.readline()

if line_number == 4:
    print(line_number)
else:
    print("No such line number")

check_file.close()

# Loops
# -----

# Exercise 1: Print First 10 natural numbers using while loop
i = 0
while i < 10:
    print(i)
    i += 1

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
t = int(input("choose a number"))
total = 0

for i in range(1, t + 1):
    total += i

print(total)

# Exercise 4: Write a program to print multiplication table of a given number
given_number = int(input("choose any number"))
for i in range(1, 10):
    product = given_number * i
    print(product)

# Exercise 5: Display numbers from a list using loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(list1)):
    print(list1[i])

# Exercise 6: Count the total number of digits in a number
input_number = input("Enter a number: ")
print(len(input_number))

# Exercise 7: Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, - 1):  # controls number of rows, from 5 to 0, decrementing by 1
    for j in range(i, 0, -1):  # controls number of columns, from i to 0, decrementing by 1
        print(j, end=" ")
    print()

# Exercise 8: Print list in reverse order using a loop
lst1 = [1, 2, 3, 4, 5, 6]
for i in range(len(lst1)):  # iterates through the list
    lst1[i] = list(str(lst1[i]))  # converts the list to strings using the str() method
    lst1[i].reverse()  # reverses the string using the reverse() method
    print(lst1[i])  # prints the reversed list

# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10, 0, +1):
    print(i)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
num = 0
if num == 0:
    print(num)
else:
    print("Done")

# Exercise 11: Write a program to display all prime numbers within a range
for i in range(2, 101):  # sets the range from 2 to 100 to check if it is a prime number
    for j in range(2, i):  # sets the range from 2 to i
        if i % j == 0:  # checks if i is divisible by j is equal to 0, then it is not a prime number
            break  # breaks the loop if i is divisible by j is equal to 0
    else:
        print(i)

# Exercise 12: Display Fibonacci series up to 10 terms
fibonacci = []
number_of_terms = 10
for i in range(0, number_of_terms):
    if i == 0:
        fibonacci.append(0)  # first element is always 0
    elif i == 1:
        fibonacci.append(1)  # second element is always 1
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])  # formula to calculate the next term
    print(fibonacci[i])

# Exercise 13: Find the factorial of a given number
n_factorial = int(input("Enter a number: "))
factorial = 1
for i in range(1, n_factorial + 1):
    factorial *= i
print(factorial)  # prints the factorial of the given number

# Exercise 14: Reverse a given integer number
opposite_integer = int(input("Enter a number: "))
print(str(opposite_integer)[::-1])
# converts the given integer number to a string using the str() method and uses negative indexing represented by
# [::-1] to reverse the integer number

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
given_list = [1, 2, 3, 4, 5, 6]
for i in range(0, len(given_list), 2):  # iterates through the list from 0 to len(given_list), every 2 indices.
    print(given_list[i + 1])

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
cubes = []
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    cubes.append(i ** 3)
    print(cubes)

# Exercise 17: Find the sum of the series upto n terms
arithmetic_sum = 0
n_terms = int(input("Enter a number: "))
for i in range(0, n_terms + 1, +1):
    arithmetic_sum += i
print(arithmetic_sum)

# Exercise 18: Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

pattern_variable = "*"
for i in range(0, 5):
    for j in range(0, i + 1):
        print(pattern_variable, end=" ")
    print()
for x in range(4, 0, -1):
    for y in range(x, 0, -1):
        print(pattern_variable, end=" ")
    print()
