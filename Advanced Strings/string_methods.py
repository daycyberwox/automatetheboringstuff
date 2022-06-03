# String Methods - Return a new string value rather than modify the old string value in place

# Upper/Lower case
spam = "Hello There"
print(spam.upper())
print(spam.lower())


# Checking if the string is upper or lower case - Returns a boolean value
print(spam.isupper())
print(spam.islower())


# Converting
print("hello".upper())
print("hello".lower())
print("hello".upper().isupper())


# isalpha() - letters only
# isalnum() - letters and numbers only
# isdecimal() - numbers only
# isspace() - whitespaces only
# istitile() - titlecase only
# startswith() - starts with a value
# endswith() - ends with a value


# Join - uses a character to join a string or list
print(",".join(['cats', 'rats', 'bats']))
print("".join(['cats', 'rats', 'bats']))
print("\n\n".join(['cats', 'rats', 'bats']))


# Splits the components of a string
print("My name is Day".split())


# Makes sure all the characters amount to the desired number in the ()
# Length justify a string
print("hello".rjust(10))   # right justify - rjust
print("hello".ljust(10)+"there!")    # left justify - ljust


# Length justify a string with any character
print("hello".rjust(10, "*"))


# Center the text
print("hello".center(20))
print("hello".center(20, "="))


# String Stripping
spam = "Hello".rjust(10)
print(spam.strip())

print("SpamSpamBaconSpamEggsSpamSpam".strip("ampS"))
# lstrip()
# rstrip()


# Replacing
spam = "Hello There"
print(spam.replace("e", "XYZ"))   # Replaces every e with xyz

