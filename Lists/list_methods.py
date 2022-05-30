# List methods


# The index method
from audioop import reverse


spam = ["hello", "hi", "hey", "howdy"]
print(spam.index("hello"))  # calling the index method for the list

name = ["Zoe", "Max", "Angie", "Max"]  # a list with duplicate items (Max)
print(name.index("Max"))   # will print the fix iteration of max in the list


# Manipulating values in a list
# Append method
spam = ["hello", "hi", "hey", "howdy"]
spam.append("yo") # adds yo to the end of the list
print(spam)


# Insert method
spam = ["hello", "hi", "hey", "howdy"]
spam.insert(1, "whaddap")  # inserts whaddap as the 1th item in the list
print(spam)


# Remove method
spam = ["hello", "hi", "hey", "howdy"]
spam.remove("hey")  # removes hey from the list
print(spam)


# Sort method
# Numerically
num = [2, 5, 3.14, 1, -7]
num.sort()   # sorts the list numerically
print(num)

# Alphabetically
animals = ["cat", "rat", "dog", "ant", "zebra", "snake", "elephant"]
animals.sort()  # sorts the list alphabetically
print(animals)


# Sort in reverse - using keywords
animals = ["cat", "rat", "dog", "ant", "zebra", "snake", "elephant"]
animals.sort(reverse=True)  # sorts the list alphabetically in reverse
print(animals)


# Sort in ASCII-betically order
name = ["Alice", "Bob", "ants", "badgers", "Carol", "cats"]
name.sort()   # sorts the list alphabetically with upper case first
print(name)


# Sort in true alphabetical order
name = ["Alice", "Bob", "ants", "badgers", "Carol", "cats"]
name.sort(key=str.lower)   # sorts the list in true alphabetical order
print(name)

