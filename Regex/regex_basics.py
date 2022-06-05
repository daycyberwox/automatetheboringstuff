# Regex Basics
# My personal favorite - https://regexr.com/


import re       # importing the regex module

message = "Call me at 415-555-3671 tomorow, or at 415-555-3671  for my office line"

# r for raw string without \ escaping and d for digits
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d")
# search datatype can be used to search a string
match = phoneNumRegex.search(message)
print(match.group())
