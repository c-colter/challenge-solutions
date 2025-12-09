"""
Solution to https://www.hackerrank.com/challenges/ip-address-validation/problem
"""

import re
from sys import stdin

lines = [l.rstrip() for l in stdin.readlines()[1:]]

ipv4 = re.compile(r'^((\d|[1-9]\d|1\d\d|2[0-5][0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-5][0-5])$')
ipv6 = re.compile(r'(((000)?[\da-f]|(00)?[\da-f]{2}|0?[\da-f]{3}|[\da-f]{4})\:){7}((000)?[\da-f]|(00)?[\da-f]{2}|0?[\da-f]{3}|[\da-f]{4})')

for l in lines:
    if ipv4.fullmatch(l):
        print("IPv4")
        continue
    elif ipv6.fullmatch(l):
        print("IPv6")
        continue
    else:
        print("Neither")
