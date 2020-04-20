#!/usr/bin/python3
import sys
import re

# The bastard less, has this for its "-h" documentation:
#
#       -hn or --max-back-scroll=n
#              Specifies  a  maximum number of lines to scroll backward.  If it
#              is necessary to scroll backward more than n lines, the screen is
#              repainted in a forward direction instead.  (If the terminal does
#              not have the ability to scroll backward, -h0 is implied.)
#
# 'n' is pretty universal AND - usually isn't 2 characters (with a number of notable
# exceptions such as sendmail) 
#
pack = sys.argv[1:]
pack += map(lambda x: x + "n", filter(lambda x: x[0] == '-' and len(x) == 2, pack))
my_re = '^\s*({})(\s.*$|$)'.format('|'.join(pack))

is_def = False
line_def = False
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

        # From man 7 man we get things like this:
        #  .I  Italics
        #
        #  .IB Italics alternating with bold
        #
        #  .IR Italics alternating with Roman
        #
        elif indent_window[0] == indent and indent_window[1] == 0:
            line_def = True

        #print(indent_window, is_def, line_def)
        #print("<{}>".format(res[1]))

        buf.append(line)
        term_indent = indent

    elif term_indent:
        #print(indent, term_indent)
        if indent > 1 and (indent < term_indent or (not is_def and indent == term_indent)):
            if (len(buf) == 2 and indent == term_indent and line_def) or len(buf) > 2:
                print('\n'.join(buf))
            buf = []
            term_indent = False
            is_def = False
        else:
            # Once our formatting goes in we have to reset it 
            if is_def and indent > term_indent:
                is_def = False
                
            buf.append(line)
