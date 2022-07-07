# open a file and save it into a "helloFile" variable
helloFile = open(r'/Users/dayspring/Desktop/test.txt')

# read the contents of the file
content = helloFile.read()
print(content)

# retruns all of the lines in the file as strings inside of a list
print(helloFile.readlines())

# close the file after reading
helloFile.close()

# write content to a file (this overwrites the contents of the file)
# first open the file in write mode
helloFile = open(r'/Users/dayspring/Desktop/test.txt', 'w')

#write content to the file
helloFile.write('Hello!!!\nLESSGO')

# close the file after writing
helloFile.close()

# write content to a file in append mode (does not overwrite)
helloFile = open(r'/Users/dayspring/Desktop/test.txt', 'a')

#write content to the file
helloFile.write('\nWe be appending stuff ya know')

# close the file after writing
helloFile.close()