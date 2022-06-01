# Dictionary Methods


eggs = {"name": "Zophie", "species": "cat", "age": "8"}

# Keys method - Shows the keys in the dictionary
print(list(eggs.keys()))

# Values method - Shows the values in the dictionary
print(list(eggs.values()))

# Items method - Shows the items in the dictionary
print(list(eggs.items()))


# Using methods in for loops
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)


# The get method
print(eggs.get("age", 0))   #  get the value of age in eggs but if it doesn't exist, print 0
print(eggs.get("height", 0))  #  get the value of height in eggs but if it doesn't exist, print 0


# Set default method
eggs.setdefault("color", "black")  # if it doesn't exit in the dictionary, set the key of color with the value of black
print(eggs)