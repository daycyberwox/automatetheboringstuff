# Using for loops with lists


supplies = ["pens", "staplers", "binders", "books"]
for supindex in range(len(supplies)):
    print("Index " + str(supindex) + " in the supplies list is: " + supplies[supindex])


# Using multiple assigments
cat = ["fat", "orange", "loud"]   #defining a list
# Assiging variables to items in an ineffective way
size = cat[0]
color = cat[1]
sound = cat[2]

# Assiging variables to items in an effective way
cat = ["fat", "orange", "loud"]
cat = size, color, sound    # this will assign each variable to a corresponding item in the list

print(size)


# Assigning multiple variables to multiple values
size, color, sound = "skinny", "black", "quiet"
print(size)



# Swapping Variables
a = "AAA"
b = "BBB"
a, b = b, a

print(a + " " + b)


# Augumented Assigment Operators
# Incrementing the value of a variable
spam = 42
spam = spam + 1  # normal way of incrementing
spam += 1 # shortcut for incrementing works for + - * / %


