#opening the file and reading it ('r')
import re
#regular expression: r: raw text. \d: digit (0-9) .: anything but new line
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
with open('./data.txt', 'r') as data:
    contents = data.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
