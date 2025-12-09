"""
Solution to https://www.hackerrank.com/challenges/find-substring/problem
"""

import re, sys

text = [i for i in sys.stdin]

num_sent = int(text[0]) # Our number of sentences
sent = text[1:1+num_sent] # Our sentences
q = [re.compile(r'\w+('+i.rstrip()+r')\w+') for i in text[2+num_sent:]] # Our query strings

for i in q:
    matches = []
    for j in sent:
        matches += re.findall(i,j)
    print(len(matches))
