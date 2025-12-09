"""
Solution to https://www.hackerrank.com/challenges/detect-html-tags/problem
"""

import re

pat = re.compile(r' *<(\w+)>?')
l=[]

n=int(input())

for i in range(n):
    s=input()
    l+=re.findall(pat,s)

l=sorted(list(set(l)))
print(';'.join(l))
