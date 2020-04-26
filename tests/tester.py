#!/usr/bin/env python3
import glob
import os
import sys
import re
import json

os.environ['MANWIDTH'] = '250'
if len(sys.argv) > 1:
    print("making test for arguments")
    args = sys.argv[1:]
    fname = re.sub(' ', '_', ' '.join(args)) + ".test"
    if os.path.exists(fname):
        print("I'm not going to overwrite {}. Please remove it then rerun this.".format(fname))
        sys.exit(-1)

    with open(fname, 'w') as f:
        print("Creating {}".format(fname))
        f.write("{}\n".format(json.dumps(args)))
        command = ' '.join(args)
        res = os.popen("../mansnip " + command).read()
        print(res)
        f.write(res)
        sys.exit(0)


for path in glob.glob("*.test"):
    with open(path, 'r') as f:
        expected = f.readlines()
        command = ' '.join(json.loads(expected[0]))
        result = expected[1:]

    cmd = "../mansnip " + command
    res = os.popen(cmd).read()
    if res == expected:
        print(cmd + "passed")
    else:
        print(cmd + "failed")


