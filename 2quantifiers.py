
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

example = '''
Mr. Sanchez
Mr VonSüßkind
Mr. Endlich
Mrs. Robinson
Ms DAVIS
Mr. T
'''

import re
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(example)
for match in matches:
    print(match)
