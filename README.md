# base64-rust
 
Getting to know rust by impemementing base64 encode/decode command line tool.

### Commands
 - ***encode***, ***e*** : Base64 encode string
 - ***decode***, ***d*** : Base64 decode string

Usage

### To compile:

    rustc letsB64.rs

### To Run
    
    ./letsB64 <COMMAND> <STRING>

### examples

    $ ./letsB64 encode "Twas brillig, and the slithy toves"
    VHdhcyBicmlsbGlnLCBhbmQgdGhlIHNsaXRoeSB0b3Zlcw==

    $ ./letsB64 decode "VHdhcyBicmlsbGlnLCBhbmQgdGhlIHNsaXRoeSB0b3Zlcw=="
    Twas brillig, and the slithy toves

	$ ./letsB64 e "Would you like a little more tea?" | xargs ./letsB64 d
	Would you like a little more tea?
