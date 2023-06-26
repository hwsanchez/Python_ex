import re
#Anchors:
# \b   -Word boundary.
# \B   -Not a word Boundary.
# ^    - Begining of a string.
# $    - End of a string.

sentence = 'Start of a sentence and then bring it to an end'

#here the pattern is a bigining of string with the text: Start
pattern = re.compile(r'Start')

#here we r looking for end at the end of a string.
pattern2 = re.compile(r'end$')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)



matches = pattern2.finditer(sentence)

for match in matches:
    print(match)
