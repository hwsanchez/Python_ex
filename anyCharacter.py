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
Mr. T

'''
#Metacharacters:
# .   - Any Character Except New Line.

pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
