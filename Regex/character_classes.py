# Character Classes

import re

# \d - for digits.
# \D - any character that is not a numeric digit from 0 to 9.
# \w - letters, numeric digits, or the underscore character. (Think of this as matching “word” characters.)
# \W - any character that is not a letter, numeric digit, or the underscore character.
# \s - any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S - any character that is not a space, tab, or newline.


# Use cases
lyrics = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
# one or more digits, space, and one or more words
xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall(lyrics))


# Making your own character class
letterRegex = re.compile(r"[a-z]")   # using ranges
letterRegex = re.compile(r"[a-f]")   # using ranges
letterRegex = re.compile(r"[a-fA-F]")

# basically searching for vowels - a or e or i or o or u (r"a|e|i|o|u")
vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("Robocop eats baby food."))

# matching 2 vowels in a row
doublevowelRegex = re.compile(r"[aeiouAEIOU]{2}")
print(doublevowelRegex.findall("Robocop eats baby food."))

# negative character class - matches every character that is NOT in the specified character list
consonantsRegex = re.compile(r"[^aeiouAEIOU]")
print(consonantsRegex.findall("Robocop eats baby food."))
