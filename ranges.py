#looking for 1-800 or 1-900 numbers:
import re

with open('./data.txt', 'r') as f:
    contents = f.read()

pattern = re.compile(r'[1-3]')
matches = pattern.finditer(contents)
for match in matches:
    print(match)

#two ranges back to back with lowercase and uppercase letters:

pattern = re.compile(r'[a-zA-Z]')

matches = pattern.finditer(contents)

for match in matches:
    print(match)

#inside of a range the caret looks for anything that is NOT in that range.

example = '''
cat
mat
bat
pat
3at
'''
#here it looks for any 3 character combi that ends in 'at' but does NOT starts with 'b'
pattern = re.compile(r'[^b]at')

matches = pattern.finditer(example)

for match in matches:
    print(match)
