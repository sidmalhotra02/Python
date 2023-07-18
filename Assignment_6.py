# Assignment 6
# ----------
# Create a function in Python
def function_name(name1):
    print(name1)
    return "Siddharth"


# Create a function with variable length of arguments
def multiple_args(*b):
    print(sum(b))
    return 10, 20


# WAP to check whether the given 2 strings are equal or not by ignoring) + the case
str1 = input("Enter the str1:\t")
Str2 = input("Enter the str2:\t")

if str1 == Str2:
    print("Both the strings are equal")
else:
    print("Both the strings are not equal")

# WAP to check whether the username and password are same or not
# username--> maheshkumar
# password-->PYTHON

username = input("Enter the username:\t")
password = input("Enter the password:\t")

if username == password:
    print("Both the username and password are same")
else:
    print("Both the username and password are not same")

# WAP to convert the first and last character of the given string as uppercase and the remaining data should be in the
# lowercase
# python - PythoN

string1 = input("Enter the string: ")

for i in range(len(string1)):
    string1 = string1[0].upper() + string1[1:5] + string1[-1].upper()

print(string1)

# WAP to calculate the largest of the given 3 numbers using lambda functions
x = 9
y = 23
z = 14

biggest = lambda number: max(x, y, z)
result = biggest(1)
print(result)


# WAP to calculate the smallest of the given 3 numbers using lambda functions
a = 5
b = 2
c = 3

smallest = lambda number: min(a, b, c)
result = smallest(1)
print(result)