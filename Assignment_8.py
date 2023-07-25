# OOPS Assignment
#
# 1) Library Management System:
#
# Description: Implement a Book class with attributes title, author, and publisher.
# Then, create a Library class that keeps a list of Book objects.
# The Library should have methods to add_book, remove_book, and find_book_by_title.
#
# Expected Output: You should be able to create Book objects, add them to a Library, remove them,and find them by title.
#
# Hint: The add_book method should append a Book to the Library's list of books.
# The remove_book method should remove a Book from the list. The find_book_by_title
# method should loop through the list of books and return the first Book that matches the given title.
#
# sample output:
# Book1 is available in the library.
# Book3 not found in the library.
# Due Dates:

class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def display(self):
        print(f"Book {self.title} is available in the library.")
        print(f"Author {self.author} is available in the library.")
        print(f"Publisher {self.publisher} is available in the library.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None  # Book not found in the library

    def remove_book(self, book):
        self.books.remove(book)


library = Library()

book1 = Book("Book1", "Author1", "Publisher1")
book2 = Book("Book2", "Author2", "Publisher2")

library.add_book(book1)
library.add_book(book2)

# Finding a book
title_to_find = "Book1"
found_book = library.find_book_by_title(title_to_find)
if found_book == library.find_book_by_title(title_to_find):
    found_book.display()
else:
    print(f"{title_to_find} not found in the library.")

    # Removing a book
    library.remove_book(book2)

    # Trying to find a removed book
    title_to_find = "Book2"
    if found_book == library.find_book_by_title(title_to_find):
        found_book.display()
    else:
        print(f"{title_to_find} not found in the library.")


#
#
# 2) Bank Account Manager:
#
# Description: Create a BankAccount class with attributes account_number, account_name, and balance.
# Include methods for deposit, withdraw, and check_balance. Make sure the withdrawal method does not allow the
# balance to go negative.
#
# Expected Output: You should be able to create BankAccount objects, deposit money into them, withdraw money
# from them (as long as the withdrawal does not exceed the balance), and check the current balance.
#
# Hint: The deposit method should increase the balance by the deposit amount.
# The withdrawal method should decrease the balance by the withdrawal amount only if the balance is sufficient.
# The check_balance method should return the current balance.
#
# sample output:
#
# Account Number: 12345
# Account Holder: John Doe
# Balance: 5000
# Account Number: 12345
# Account Holder: John Doe
# Balance: 6000
# Account Number: 12345
# Account Holder: John Doe
# Balance: 3000
#

class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_name}")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds. Please try again.")

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_name}")
        print(f"Balance: {self.balance}")


# starting bank account
Account1 = BankAccount(account_number=12345, account_name="John Doe", balance=5000)

# depositing money into account
Account1.deposit(1000)

# withdrawing money from account
Account1.withdraw(9000)

# checking account balance
Account1.check_balance()

#
# 3)Student Grade Calculator:
#
# Description: Implement a Student class with attributes name, id, and a list of grades. The Student class should have
# methods to add_grade, calculate_average, and determine_letter_grade.
#
# Expected Output: You should be able to create Student objects, add grades to them, calculate the average of their
# grades, and determine their letter grade based on the average.
#
# Hint: The add_grade method should append a grade to the Student's list of grades. The calculate_average method
# should return the average of the grades in the list. The determine_letter_grade method should return a letter grade
# (A, B, C, etc.) based on the average grade.
#
# sample output:
#
# Student Name: John Doe
# Roll Number: 12345
# Marks: 85
# Grade: A
# Student Name: John Doe
# Roll Number: 12345
# Marks: 90
# Grade: A+

class Student:
    def __init__(self, name, id, grades=None):
        self.grade = list()
        self.name = name
        self.id = id
        if grades is not None:
            self.grade = grades

    def add_grade(self, grade):
        self.grade.append(grade)
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.id}")
        print(f"Marks: {grade}")

    def calculate_average(self):
        return sum(self.grade) / len(self.grade)

    def determine_letter_grade(self):
        if self.calculate_average() >= 90:
            return "Grade: A+"
        elif self.calculate_average() >= 80:
            return "Grade: A"
        elif self.calculate_average() >= 70:
            return "Grade: B"
        elif self.calculate_average() >= 60:
            return "Grade: C"
        elif self.calculate_average() >= 50:
            return "Grade: D"
        else:
            return "Grade: F"


std1 = Student(name="John Doe", id=12345, grades=[85])

std1.add_grade(90)
std1.add_grade(85)

average = std1.calculate_average()
letter_grade = std1.determine_letter_grade()

print(f"Average: {average}")
print(letter_grade)

