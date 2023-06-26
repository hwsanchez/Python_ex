#to use regular expressions we need to import re:
import re

#Multi-line string declaration:

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

#Raw String: string prefixed with an 'r'. Raw strings dont handle backslashes in any special way.
print('\tTab')
print(r'\tTab')

#the re.compile function allows to separate string patterns into a variable and make it easier to reuse that variable for multiple seraches.
#the variable patter contains the raw string pattern: 'dal'
pattern = re.compile(r'dal')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[50:53])
print(text_to_search[129:132])
print(text_to_search[132:135])
print(text_to_search[136:139])
#result:
# <re.Match object; span=(50, 53), match='dal'>
# <re.Match object; span=(129, 132), match='dal'>
# <re.Match object; span=(132, 135), match='dal'>
# <re.Match object; span=(136, 139), match='dal'>
