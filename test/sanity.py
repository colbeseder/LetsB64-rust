#!/usr/bin/env python3

import sys, subprocess, json

test_file_location = sys.argv[1]

def cmd(commands):
    r = ""
    try:
        r = subprocess.check_output(commands, stderr=subprocess.STDOUT)
        return 0, r
    except Exception as e:
        return 1, r

# bash, expected code, expected output
with open(test_file_location) as json_file:
    tests = json.load(json_file)

for test in tests:
    code, result = cmd(test[0])
    if code != test[1] or (code == 0 and test[2] != result.decode("utf-8").strip()):
        print("Fail!")
        print([code, result])
        print (test)
        exit(1)

print("All tests passed!\n")
