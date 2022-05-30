# Slice



# A slice has 2 indexes inside of it
listThree = ["cat", "rat", "dog", "elephant"]
print(listThree[1:3])   # Starts at index 3 and ends at but does not include index 3

# Adding an item to the list using an index
listThree[1] = "goat"  # Adds goat as the 1th item in the list
print(listThree)

# Replacing multiple items to the list using an indexes
listThree[1:3] = ["cow", "fish", "snake"]  # will replace items between 1 and 3 (not including 3) with the new items
print(listThree)

listThree[:2] = ["cow", "fish", "snake"]  # will replace items between 0 and 2 (not including 2) with the new items
print(listThree)

print(listThree[1:]) # print all the values not including the 1th item up to the end of the list