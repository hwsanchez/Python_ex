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

#look for the phone numbers:

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#result:
# <re.Match object; span=(1, 13), match='323-454-2331'>
# <re.Match object; span=(14, 26), match='234-556-7788'>
# <re.Match object; span=(27, 39), match='765ö676ä7776'>
