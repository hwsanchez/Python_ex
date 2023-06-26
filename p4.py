#looking for 1-800 or 1-900 numbers:
import re
longstring = '''
234-555-6756
345.344.5432
123+231+5678
1-800-123-333-4545
1.900.344.565.5678
1'800-237-876-9999
1-876-345-245-6754

'''

with open('./data.txt', 'r') as f:
    contents = f.read()

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(contents)
for match in matches:
    print(match)
