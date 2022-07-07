import os #the os module contains lots of file path related functions

# Using strings to represent file paths and file names

# notice the use of double backslashes for escaping
print('c:\\spam\\eggs.png')

# using raw strings
print(r'c:\spam.eggs.png')

# using the join method to join multiple file paths
print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

# get current working directory
print(os.getcwd())

# change current working directory
# print(os.chdir(r'/Users/dayspring/Desktop/Repos/'))

# check if a file path exists
# print(os.path.exists(r'../dayspring/Desktop/BlackHat'))

# check if something is a file
# print(os.path.isfile(r'file or folder name'))

# check if something is a folder/directory
# print(os.path.isdir(r'file or folder name'))

# check the size in bytes of a file
file = r'/Users/dayspring/Desktop/'
print(os.path.getsize(file))

# list the contents of a directory/folder
print(os.listdir(file))

# make a new folder or directory
os.makedirs(r'/Users/dayspring/Desktop/bulloks')