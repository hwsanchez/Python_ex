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
# .   - Any character Except newline.
# \d  - Digit: 0-9

print('DIGIT:')
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# \D   - not a digit: anything other than 0-9
print('NOT A DGIT:')
pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
