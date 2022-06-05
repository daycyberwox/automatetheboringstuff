# Regex Groups


import re       # importing the regex module

message = "Call me at 415-555-3671 tomorow, or at 415-555-3671  for my office line"

# paranthesis used to mark out various groups
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d)")
match = phoneNumRegex.search(message)
print(match.group(1))   # group 1 covers the first pair paranthesis
print(match.group(2))


# Escaping actual paranthesis with \
call = "Call me at (415) 555-3671"
newNumRegex = re.compile(r"\(\d\d\d\) \d\d\d-\d\d\d")
num = newNumRegex.search(call)
print(num.group())
