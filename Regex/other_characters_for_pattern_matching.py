

import re
# ^ specifies that the string has to begin with the proceeding word
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search("Hello there"))


# $ specifies that the string has to begin with the preceeding word
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search("Hello world!"))


# matching the entire string
# matches one or more digits & must start and end with digits
allDigitsRegex = re.compile(r"^\d+$")
print(allDigitsRegex.search("238278373847808392832732938789"))

# DOT
# . - matches any single character except a new line
atRegex = re.compile(r".at")
story = "The cat in the hat sat on the flat mat while eating the rat"
print(atRegex.findall(story))  # matches cat, hat, sat and so on

# matching multiple
atRegex = re.compile(r".{1,2}at")   # or 2 preceeding characters
story = "The cat in the hat sat on the flat mat while eating the rat"
print(atRegex.findall(story))  # matches cat, hat, sat and so on


# DOT STAR
# .* - matches ANY preceeding pattern whatsoever (uses greedy mode)
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
info = "First Name: Al Last Name: Sweigart"
print(nameRegex.findall(info))

# .*? - non greedy variant
serve = "<To serve humans> for dinner."
nongreedyRegex = re.compile(r"<(.*?)>")
print(nongreedyRegex.findall(serve))
# greeedy
server = "<To serve humans> for dinner."
greedy = re.compile(r"<(.*)>")
print(greedy.findall(server))


# (.*, re.DOTALL) - matches ANY preceeding pattern whatsoever (uses greedy mode)
# without DOTALL
prime = "Serve the public trust.\nProtect the innocent.\nUpload the law."
dotStar = re.compile(r".*")
print(dotStar.search(prime))   # only matches up to the end of the first line


# DOTALL
dotStar = re.compile(r".*", re.DOTALL)    # matches everything including spaces
print(dotStar.search(prime))


# DOT IGNORECASE
vowelRegex = re.compile(r"[aeiou]")
# ignores case sensitivity or re.I
vowelRegex = re.compile(r"[aeiou]", re.IGNORECASE)
print(vowelRegex.findall("Robocop eats baby food."))
vowelRegex = re.compile(r"[aeiou]", re.I)
print(vowelRegex.findall("Robocop eats baby food."))
