#  Matching repetitions


import re


# ? - the preceding group () can appear in the text 0 or 1 time in order to match the pattern
batRegex = re.compile(r"Bat(wo)?man")

match = batRegex.search("The Adventures of Batman")
print(match.group())

match = batRegex.search("The Adventures of Batwoman")
print(match.group())


# Phone number
# ? makes the preceding group optional - can either appear once or 0 times
phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
match = phoneRegex.search("My phone number is 555-1234. Call me tomorrow!")
print(match.group())


# * - matches 0 or more times
# * matches for if (wo) appears 0 or more times
catRegex = re.compile(r"Cat(wo)*man")

match = catRegex.search("The Adventures of Catman")
print(match.group())

match = catRegex.search("The Adventures of Catwoman")
print(match.group())


# + - matches 1 or more times (at least once)
fatRegex = re.compile(r"Fat(wo)+man")

# match = fatRegex.search("The Adventures of Fatman") - will result in a failure since "wo" doesn't appear at least once
# print(match.group())

match = fatRegex.search("The Adventures of Fatwoman")
print(match.group())


# Escaping special characters
regex = re.compile(r"\+\*\?")
reg = regex.search("I learned about +*? regex syntax.")
print(reg.group())
