#quantifiers help avoid repeating backslashes

# Quantifiers:
# *   - 0 or More
# +   - 1 or More
# ?   - 0 or One
# {3} - Exact number: 3
# {4,5} - Range of numbers: Minimum, Maximum
#
# here for the telephon number example:

import re
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
with open('./data.txt', 'r') as f:
    content = f.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)

#only 800 and 900 numbers:
print('*************** Only 800 and 900 *********************')
pattern = re.compile(r'[89]00.\d{3}.\d{4}')
matches = pattern.finditer(content)
for match in matches:
    print(match)
