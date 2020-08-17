![Run tests](https://github.com/colbeseder/LetsB64-rust/workflows/All%20Tests/badge.svg?branch=master)

# base64-rust
 
Getting to know Rust by impemementing base64 encode/decode command line tool.

### Commands
 - ***encode***, ***e*** : Base64 encode string
 - ***decode***, ***d*** : Base64 decode string

Usage

### To compile:

    rustc letsB64.rs

### To Run
    
    ./letsB64 <COMMAND> <STRING>

### Examples

    $ ./letsB64 encode "Twas brillig, and the slithy toves"
    VHdhcyBicmlsbGlnLCBhbmQgdGhlIHNsaXRoeSB0b3Zlcw==

    $ ./letsB64 decode "VHdhcyBicmlsbGlnLCBhbmQgdGhlIHNsaXRoeSB0b3Zlcw=="
    Twas brillig, and the slithy toves

	$ ./letsB64 e "Would you like a little more tea?" | xargs ./letsB64 d
	Would you like a little more tea?

### Tests

    $ ./sanity.py
    All tests passed!