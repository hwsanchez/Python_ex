#Regular Expressions: Anchors: They DONT match any CHARACTERS
#but invisible positions before or after characters

#Anchors:
# \b   -Word boundary. Word boundaries are indicated by whitespace OR non alpha numeric characters
# \B   -Not a word boundary
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

Ha HaHa

Mr. Paul
Mr Schmidt
Ms Tabano
Mrs Macana
Mr. T

'''

#here the Anchor will look for appearances of 'Ha' at the begining of a word (\b = word boundary)
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#result:
# <re.Match object; span=(210, 212), match='Ha'>
# <re.Match object; span=(213, 215), match='Ha'>
#notice it found 2 'Ha'. It ignored the one that is not at the begining of the word.
