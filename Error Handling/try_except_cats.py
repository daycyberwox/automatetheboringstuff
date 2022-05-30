print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That's a lotta cats.")
    elif int(numCats) < 0:
        print("Please enter a positive integer")
    else:
        print("That's not that many cats.")
except ValueError:
    print("""You did not enter a number. 
             Please enter a number""")