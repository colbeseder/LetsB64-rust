import subprocess

def cmd(commands):
    r = ""
    try:
        r = subprocess.check_output(commands, stderr=subprocess.STDOUT)
        return 0, r
    except Exception as e:
        return 1, r

# bash, expected code, expected output
tests = [
    #Compile
    [["rustc", "letsB64.rs"], 0, ""],
    # No args
    [["./letsB64"],           1, ""],
    # Not enough args
    [["./letsB64", "e"],      1, ""],
    # Command doesn't exist
    [["./letsB64", "f"],      1, ""],
    # Wrong length for decode
    [["./letsB64", "d", "a="],1, ""],

    #Encoding
    [["./letsB64", "encode", ""                         ], 0, ""],
    [["./letsB64", "e",      ""                         ], 0, ""],
    [["./letsB64", "e",      "a"                        ], 0, "YQ=="],
    [["./letsB64", "e",      "be"                       ], 0, "YmU="],
    [["./letsB64", "e",      "see"                      ], 0, "c2Vl"],
    [["./letsB64", "e",      "ddee"                     ], 0, "ZGRlZQ=="],
    [["./letsB64", "e",      "welcome!"                 ], 0, "d2VsY29tZSE="],
    [["./letsB64", "e",      "I'm feeling great"        ], 0, "SSdtIGZlZWxpbmcgZ3JlYXQ="],

    #Decoding
    [["./letsB64", "decode", ""                         ], 0, ""],
    [["./letsB64", "d",      ""                         ], 0, ""],
    [["./letsB64", "d",      "YQ=="                     ], 0, "a"],
    [["./letsB64", "d",      "YmU="                     ], 0, "be"],
    [["./letsB64", "d",      "c2Vl"                     ], 0, "see"],
    [["./letsB64", "d",      "ZGRlZQ=="                 ], 0, "ddee"],
    [["./letsB64", "d",      "d2VsY29tZSE="             ], 0, "welcome!"],
    [["./letsB64", "d",      "SSdtIGZlZWxpbmcgZ3JlYXQ=" ], 0, "I'm feeling great"]
]

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
