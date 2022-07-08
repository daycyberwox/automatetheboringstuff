import os

# Pass a root folder and iterate all the contents of the folder
for folderName, subfolders, filenames in os.walk(r'/Users/dayspring/Desktop/delecious'):
        print('The folder is ' + folderName)
        print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
        print('The filenames in ' + folderName + ' are: ' + str(filenames))
        print()

        for subfolder in subfolders:
            print(subfolder)

        # doing a dry run to prevent unwanted file deletion
        for subfolder in subfolders:
            if 'fish' in subfolder:
                #os.rmdir(subfolder)
                print('rmdir on' + subfolder)

        for file in filenames
            if file.endswith('.py'):
                shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')