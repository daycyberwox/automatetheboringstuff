# Find all regex method


import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
contact = 'Cell: 415-555-9999 Work: 212-555-0000'
# findall returns a list of strings that match the defined pattern
print(phoneRegex.findall(contact))


# Example 1
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
contact = 'Cell: 415-555-9999 Work: 212-555-0000'
print(phoneRegex.findall(contact))


# Example 2
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
contact = 'Cell: 415-555-9999 Work: 212-555-0000'
print(phoneRegex.findall(contact))
