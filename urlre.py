import re

#multi-line string:

text_to_search = '''
ging.com
hwsanchez.com
googledotcom
'''

#here we escaple the meta character period (.) to find an url:
pattern = re.compile(r'ging\.com')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
