# A better while loop that uses a #break 


name = ''
while True:
    print("Please type your name")
    name = input()
    if name == "Day":
        break
    elif name == '':
        print("You have not entered a valid name!\n")
print("Thank you!")