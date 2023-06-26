# Quantifiers:
# *   - 0 or More
# +   - 1 or More
# ?   - 0 or One
# {3} - Exact number: 3
# {4,5} - Range of numbers: Minimum, Maximum


# .   - Any characters
# \d  - Any digit : 0-9
# \D  - Not a digit.
# \w  - Word character: a-z, A-Z, 0-9, _
# \W  - Not a Word character.
# \s  - whitespace: space, tab, newline


#Regular Expressions: Anchors: They DONT match any CHARACTERS
#but invisible positions before or after characters

#Anchors:
# \b   -Word boundary. Word boundaries are indicated by whitespace OR non alpha numeric characters
# \B   -Not a word boundary


emails = '''
hwsanchez@me.com
hwsanchez.poreda@gmail.com
john-123-macana@mafia.net
HarryMcAna@mcana-family.net'''

import re
pattern = re.compile(r'[a-zA-Z\d.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
