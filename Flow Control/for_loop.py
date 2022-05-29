# For loops


# New line function
def nl():
    print("\n")

print("My name is")
for x in range(5):
    print("Jimmy Five Times "+ str(x))
nl()

# Adding up to 100!
total = 0
for num in range(101):  #every number between 0 and 101 but not including 101
    total = total + num
print(total)
nl()

# Using steps
for y in range(0, 10, 2):
    print("This is stepping with "+str(y)+" intervals")
nl()


for z in range(5, -1, -1):
    print("This is stepping with "+str(z)+" intervals")
