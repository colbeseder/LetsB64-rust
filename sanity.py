#!/usr/bin/env python3

import subprocess, json

def cmd(commands):
    r = ""
    try:
        r = subprocess.check_output(commands, stderr=subprocess.STDOUT)
        return 0, r
    except Exception as e:
        return 1, r

# bash, expected code, expected output
with open('tests.json') as json_file:
    tests = json.load(json_file)

# Delete old binary to ensure that we're testing latest code
cmd(["rm", "letsB64"])

for test in tests:
    code, result = cmd(test[0])
    if code != test[1] or (code == 0 and test[2] != result.decode("utf-8").strip()):
        print("Fail!")
        print([code, result])
        print (test)
        exit(1)

print("All tests passed!\n")
