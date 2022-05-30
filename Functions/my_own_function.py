# Writing your own functions

# Function 1
from tkinter import N


def nl():
    print("\n")
    print("-" * 50)

# Function 2
def hello():  #defining the function
    print("Howdy!")
    print("Hey There!")
hello()
nl()

# Function 3
def hello(name): # passing an argument to the function
    print("Hello "+name)

hello("Alice")
hello("Day")
nl()

# Function 4
def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

