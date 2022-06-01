# Character Counter

import pprint # module for "pretty print"

print("What text would you like to count?")

message = input()
count = {}  # empty dictionary

for character in message:       # for each character in message - use message.upper()/message.lower() as preferred
    count.setdefault(character, 0)    # assign a value of 0 to each 
    count[character] = count[character] + 1 # create a key value pair list of each character that exists with an increment of 1 for each value

pprint.pprint(count)  #using the pprint module/function

#text = pprint.pformat(count)  # another option
#print(text)