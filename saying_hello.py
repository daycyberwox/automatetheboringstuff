# This program says hello and asks for a name

print("Hello there!")

print("What is your name?") # asks for a name
Name = input() #user inputs a name that will be stored in the myName variable
print("It's good to meet you, "+Name)
print("The length of your name is "+str(len(Name))+" characters")

print("What is your age?") # asks for their age
Age = input()
print("You will be "+str(int(Age) + 1)+" in a year!")

