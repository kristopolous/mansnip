#!/usr/bin/python3
import sys
import re

my_re = '^\s*({})(\s.*$|$)'.format('|'.join(sys.argv[1:]))

is_def = False
buf = []
term_indent = False
indent_window = []

for line in sys.stdin:
    line = line.strip('\n')
    indent = re.match('^(\s*)', line).end()
    indent_window = indent_window[-2:] + [indent]

    res = re.match(my_re, line)
    if res:
        # This is sheer frantic handwaving for things like this (From bash)
        #
        #  declare [-aAfFgilnrtux] [-p] [name[=value] ...]
        #  typeset [-aAfFgilnrtux] [-p] [name[=value] ...]
        #
        # Surely, if I search for "declare" this is what I want, but it
        # it breaks our classic rules so instead we try a number of 
        # imperfet guesses.
        #
        # The first one is back-searching the indent margins. Generally
        # there's a space before we see this and then some end of a 
        # previous block that was indented further. soooo yeah we
        # look for that.
        #
        if indent_window[0] > indent and indent_window[1] == 0:
            is_def = True

        #print(indent_window, is_def)
        #print("<{}>".format(res[1]))

        buf.append(line)
        term_indent = indent

    elif term_indent:
        #print(indent, term_indent)
        if indent > 1 and (indent < term_indent or (not is_def and indent == term_indent)):
            if len(buf) > 2:
                print('\n'.join(buf))
            buf = []
            term_indent = False
            is_def = False
        else:
            # Once our formatting goes in we have to reset it 
            if is_def and indent > term_indent:
                is_def = False
                
            buf.append(line)
