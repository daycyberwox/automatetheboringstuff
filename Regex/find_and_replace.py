# Finding and replacing in regex


import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

# Find and replace
# Using a sub method - substitute
result = namesRegex.sub(
    'REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

# / syntax
# first letter of the agents name - 1 word character(\w) followed by zero or more letter characters(\w*)
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))


result = namesRegex.sub(
    r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)
