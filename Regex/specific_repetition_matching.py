# Matching a pattern for specific/desired amount of times or range of times


import re
haRegex = re.compile(r"(Ha){3}")  # match Ha exactly 3 times
ha = haRegex.search("He said HaHaHa")
print(ha.group())


# Match 3 phone numbers in a row
# Match a phone number that may or may not have an area code, exactly 3 times
phoneRegex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}")
num = phoneRegex.search("My numbers are 415-555-1234,555-4242,212-555-0000")
print(num.group())


# Match a pattern for a range of times {x,y} - at least x, at most y
naRegex = re.compile(r"(Na){3,5}")  # at least 3 times, at most 5 times
na = naRegex.search("He said NaNaNa")
print(na.group())


digitRegex = re.compile(r"(\d){3,5}")  # match anywhere between 3 & 5 digits
# will match a greedy pattern of 5 digits - the longest possible string that matches the defined pattern {3,5}
dig = digitRegex.search("1234567890")
print(dig.group())


# Non greedy match
cyberRegex = re.compile(r"(\d){3,5}?")
# will match a greedy pattern of 3 digits - the smallest possible string that matches the defined pattern {3,5}
cyber = cyberRegex.search("1234567890")
print(cyber.group())
