# Dictionaries - A collection of multiple key value pairs stored in {} - curly braces


myCat = {'size':'fat', 'color':'green', 'dispostion':'loud'}
print(myCat['size'])    # access values through keys 
print("My cat has " + myCat['color'] + " fur.")     # concatonating


# Dictionaries have no order compared to list
[1, 2, 3] == [3, 2, 1]   # an unordered list that will be False

eggs = {"name": "Zophie", "species": "cat", "age": "8"}
ham = {"species": "cat", "age": "8", "name": "Zophie"}
eggs = ham   #  Will be true regardless of unordered dictionaries


# Check if a key exists in a dictionary
print("name" in eggs)
print("name" not in eggs)