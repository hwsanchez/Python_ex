#to use regular expressions we need to import re:
import re

#Multi-line string declaration:

text_to_search = '''

META CHARACTERS (NEED TO BE ESCAPED):
^ $ * + ? { } [ ] / | ( ) .

Hola.

'''

#if we are looking for iterances of any meta character we need to escape it; this bellow will not work:
#this is because meta characters have special meaning in regular expressions!
pattern = re.compile(r'.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#to avoid this we need to escape the meta character with a black slash in front:

pattern = re.compile(r'\.')

matches = pattern.finditer(text_to_search)
print('----------------Escaped!--------------------')
for match in matches:
    print(match)
