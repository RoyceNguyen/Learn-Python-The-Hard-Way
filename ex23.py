import sys
script, encoding, error = sys.argv

#define function which takes arguments
def main(language_file, encoding, errors):
    #read one line from the language_file it's given
    line = language_file.readline()
    #if line had a value, then run the code
    if line:
        #call a seperate function to do the actual printing
        print_line(line, encoding, errors)
        #calling a function inside of itself, creating a loop(recursion) 
        #that runs as long as if statement is true
        return main(language_file, encoding, error)
#definding print_Line function which handles the encoding and decoding 
def print_line(line, encoding, errors):
    #strip the trailing \n\ on the line string
    next_lang = line.strip()
    #DBES, "DECODE BYTES, ENCODE STRINGS"
    #next_lang is a string so to get raw bytes you must encode() to "Encode Strings"
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #doing the inverse of DBES, raw_bytes is bytes so call decode() "Decode Bytes" 
    # in order to get a string, 
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #print out both variables
    print(raw_bytes, "<===>", cooked_string)
#open the languages.txt file
languages = open("languages.txt", encoding="utf-8")
#run the main function with all the params and start the loop
main(languages, encoding, error)
