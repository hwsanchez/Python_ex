#character set: put the specific characters you want to match inside the square brackets:
import re
longstring = '''
234-555-6756
345.344.5432
123+231+5678
'''

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(longstring)

for match in matches:
    print(match)
