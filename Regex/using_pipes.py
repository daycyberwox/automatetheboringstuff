# Using the pipe character |

import re

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
match = batRegex.search("Batmobile lost a wheel")
print(match.group())
