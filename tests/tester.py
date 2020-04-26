#!/usr/bin/env python3
import glob
import os

os.environ['MANWIDTH'] = '50'
for path in glob.glob("*.test"):
    with open(path, 'r') as f:
        expected = f.readlines()
        command = expected[0]
        result = expected[1:]

    cmd = "../mansnip " + command
    res = os.popen(cmd).read()
    if res == expected:
        print(cmd + "passed")
    else:
        print(cmd + "failed")


