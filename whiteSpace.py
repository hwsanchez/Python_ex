import re
text_to_search = '''
323-454-2331
234-556-7788
765ö676ä7776

safhjfhljdalfjkvjfnvjnfdjlndfjvndlfieö
SADHAHDÖAHFHHWFEQPEHPQHWFIURUEHNVÖÖÖ
1234567890

daldal dal Dal

META CHARACTERS (NEED TO BE ESCAPED):
^ $ * + ? { } [ ] / | ( )

Mr. Paul
Mr Schmidt
Ms Tabano
Mrs Macana
    Rikiti  &   Flikiti
Mr. T
    iterances   iterances   hhj
'''

# .   - Any characters
# \d  - Any digit : 0-9
# \D  - Not a digit.
# \w  - Word character: a-z, A-Z, 0-9, _
# \W  - Not a Word character.
# \s  - whitespace: space, tab, newline

pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
for match in  matches:
    print(match)
