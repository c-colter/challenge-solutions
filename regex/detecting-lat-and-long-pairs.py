"""
Solution to https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
"""

import re, sys

lines = sys.stdin.readlines()[1:]
pat = re.compile(r'\((\+|-)?(90(\.0+)?|[1-8]?[0-9](\.\d+)?), (\+|-)?(180(\.0+)?|1[0-7][0-9](\.\d+)?|[1-9]?[0-9](\.\d+)?)\)')

for l in lines:
    print("Valid") if pat.match(l) else print("Invalid")
