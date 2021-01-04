#!/usr/bin/env python3
import os
import sys
import re
import tempfile
import time
import subprocess
import json

os.environ['MANWIDTH'] = '250'
os.environ['MANSNIP_TESTING_NOLINES'] = '1'

tempdir = None
test_filter = None
def params_to_fname(params):
    return re.sub(' ', '_', params) + ".test"

def store_results(path, expected, actual):
    global tempdir
    if not tempdir:
        tempdir = tempfile.mkdtemp()
        print("      Using {} for failures".format(tempdir))

    with open("{}/{}-expected".format(tempdir,path), 'w') as f:
        f.write(expected)

    with open("{}/{}-actual".format(tempdir,path), 'w') as f:
        f.write(actual)

if len(sys.argv) == 2:
    with open('testlist.txt', 'r') as f:
        testList = f.read().splitlines()

        for testraw in testList:
            testList = json.loads(testraw)
            test = ' '.join(testList)
            print(test)

    sys.exit(0)

if len(sys.argv) > 2:
    args = sys.argv[1:]
    test_filter = ' '.join(args)
    fname = "tests/" + params_to_fname(test_filter)

    if os.path.exists(fname):
        sys.stderr.write("I'm not going to overwrite {}. If you want to replace it then remove it and this.\n".format(fname))
        sys.stderr.write("Running single test.\n")
        
    else:
        sys.stderr.write("making test for arguments\n")
        with open('testlist.txt', 'a') as f:
            f.write(json.dumps(args) + "\n")

        with open(fname, 'w') as f:
            print("Creating {}".format(fname))

            p = subprocess.Popen(['../mansnip'] + args, stdout=subprocess.PIPE)
            res = p.communicate()[0].decode("utf-8")

            print(res) 
            f.write(res)
            sys.exit(0)

with open('testlist.txt', 'r') as f:
    testList = f.read().splitlines()

    for testraw in testList:
        testList = json.loads(testraw)
        test = ' '.join(testList)
        if test_filter and test_filter != test:
            continue

        if test == 'stop':
            print("asked to stop")
            sys.exit(0)

        if test[0] == '#':
            print("skipping {}".format(test))
            continue

        fname = params_to_fname(test)

        with open("tests/" + fname, 'r') as f:
            expected = f.read()

        start = time.time()
        p = subprocess.Popen(['../mansnip'] + testList, stdout=subprocess.PIPE)
        actual = p.communicate()[0].decode("utf-8")
        runtime = "{:#.3f}".format(time.time() - start)

        if actual == expected:
            print(runtime + "    OK     " + test)
        else:
            store_results(fname, expected, actual)
            print(runtime + " !! FAILED " + test)


