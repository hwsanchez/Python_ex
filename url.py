import re


url = '''
https://www.google.com
http://starwars.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.com|\.gov)')

subbed_urls = pattern.sub(r'\2\3', url)

print(subbed_urls)
