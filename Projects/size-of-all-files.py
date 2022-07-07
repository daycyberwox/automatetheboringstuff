# A simple programs to find the total size of all files in a folder
file = r'/Users/dayspring/Desktop/'

totalSize = 0
for filename in os.listdir(r'/Users/dayspring/Desktop/'):
    if not os.path.isfile(os.path.join(r'/Users/dayspring/Desktop/', filename))
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(r'/Users/dayspring/Desktop/', filename))
print(totalSize)