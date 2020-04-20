#!/usr/bin/python3

import sys
import re

term = sys.argv[1]
my_re = '^\s*{}(\s.*$|$)'.format(term)

is_def = False
buf = []
term_indent = False

for line in sys.stdin:

    line = line.strip('\n')
    indent = re.match('^(\s*)', line).end()

    res = re.match(my_re, line)
    if res:
        #print("<{}>".format(res[1]))
        buf.append(line)
        term_indent = indent

    elif term_indent:
        #print(indent, term_indent)
        if indent > 1 and indent <= term_indent:
            if len(buf) > 2:
                print('\n'.join(buf))
            buf = []
            term_indent = False
        else:
            buf.append(line)
