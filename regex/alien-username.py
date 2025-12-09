"""
Solution to https://www.hackerrank.com/challenges/alien-username/problem
"""

import re
import sys

pat = re.compile(r'^[_\.]\d+[a-zA-Z]*_?$')

for l in sys.stdin.readlines()[1:]:
    print("VALID") if re.match(pat,l) else print("INVALID")
