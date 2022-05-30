# Lists

# A list is a value that contains multiple values (items)

# Uses square brackets - []

listOne = ["cat", "rat", "dog", "elephant"]
print(listOne) # prints the items in the list

# Print the item with the specified indessx
print(listOne[1])
print(listOne[0])

# Length of a list
print(len(listOne))


# Concatonating lists
listTwo = ["Yes", "No"]
print(listOne + listTwo)


# List replication
print(listTwo * 3)


#List function
print(list("Hello"))


# Confirming if a value is in a list
yesornah = "howdy" in ["hello", "hi", "howdy", "heya"]
print(yesornah)  # Should be true

nahhh = 42 in ["hello", "hi", "howdy", "heya"]
print(nahhh) # Should be false



# Confirming if a value is NOT in a list
yesornah1 = "howdy" not in ["hello", "hi", "howdy", "heya"]
print(yesornah1)  # Should be false

nahhh1 = 42 not in ["hello", "hi", "howdy", "heya"]
print(nahhh1) # Should be true

