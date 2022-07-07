# Storage data such lists and dictionaries in "shelves" (binary file)

import shelve
shelfFile = shelve.open('HiddenLeaf')
shelfFile['shinobi'] = ['Naruto', 'Sasuke', 'Kakashi', 'Minato']
shelfFile.close()


shelfFile = shelve.open('HiddenLeaf')
print(shelfFile['shinobi'])

#list the keys and values in the shelve file
list(shelfFile.keys())
list(shelfFile.values())


shelfFile.close()