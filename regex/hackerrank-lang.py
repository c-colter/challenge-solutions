"""
Solution to https://www.hackerrank.com/challenges/hackerrank-language/problem
"""

import re
import sys

pat_api = re.compile(r"\d{4,5} (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$")

for l in [i for i in sys.stdin][1:]:
    print("VALID") if pat_api.match(l) else print("INVALID")
