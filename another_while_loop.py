# Another while loop, this time using continue


spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
     continue # skip
    print("spam is "+str(spam))