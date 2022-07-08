import os
# Note that these deletes permanently deletes affected files without sending them to the recycle bin or trash

# Delete a single file
os.unlink(r'../../delete.txt')

# Delete an empty folder
os.rmdir(r'../../Delete')

# Delete a folder and all its contents
import shutil
shutil.rmtree(r'../../Delete')


# Avoiding permanent deletions by sending to recycle bin or trash
# Mac install - python3 -m pip install -U send2trash
import send2trash
send2trash.send2trash(r'../../renamed.txt')