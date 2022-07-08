# Using the shutil function lets you copy and move stuff around
import shutil

# copy file from source location to destination location
shutil.copy(r'/Users/dayspring/Desktop/test.txt', r'/Users/dayspring/Desktop/Repos')

# copy (and rename) file from source location to destination location
shutil.copy(r'/Users/dayspring/Desktop/test.txt', r'/Users/dayspring/Desktop/Repos/destfile.txt')

# copy folder from source location to destination location
shutil.copytree(r'/Users/dayspring/Desktop/', r'/Users/dayspring/Desktop/Backup')

# move a file to a new location
shutil.move(r'/Users/dayspring/Desktop/test.txt', r'/Users/dayspring/Desktop/Repos')

# rename a file in its current location
shutil.move(r'/Users/dayspring/Desktop/test.txt', r'/Users/dayspring/Desktop/renamed.txt')