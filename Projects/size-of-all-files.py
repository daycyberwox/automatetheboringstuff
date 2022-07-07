# A simple programs to find the total size of all files in a folder
file = r'/Users/dayspring/Desktop/'

totalSize = 0
for filename in os.listdir(file):
    if not os.path.isfile(os.path.join(file, filename))
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(file, filename))
print(totalSize)