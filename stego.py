# -*-Coding:Utf-8-*-

import sys
import getopt

"""
Author: OurBinariArc
Project: CTF
Program: stego.py
Version: 1.0
Date: 15-Aug-2022
This script extracts the last n LSB of a hex or binary file and combines them into an output file.
"""

def usage():
    print(" - Steganography LSB extractor tool - ")
    print("This script extracts the last n LSB of a hex or binary file and combines them into an output file.")
    print("")
    print("Usage: stego.py -i input_file -o output_file -l length -e extract_bit")
    print("-i --input        - Input file")
    print("-o --output       - Output file")
    print("-l --length       - Length of the words in input file (2 for hex file, 8 for binary file), must be separated by space")
    print("-e --extract      - number of Least Significant Bit (LSB) to extract from the words")
    print("")
    print("")
    print("Examples:")
    print("python3 stego.py -i input.bin -o output.bin -l 8 -e 2")
    print("python3 stego.py -i input.hex -o output.hex -l 2 -e 1")
    sys.exit(0)

def createFile(file):
    f = open(file, 'w')
    f.close()

def extractNByte(file, p, n):
    with open(file, 'r') as f:
        # Read the first line of the file and stores it in an array. Words have to be separated by spaces.
        # Where p is the length of the words expected and n is the number of LSB to extract.

        line = f.readline()
        f.close()
        words = line.split()
        reconstruct = []
        for w in words:
            # Check if the length of the words is valid.
            if len(w) != p:
                print("Error format: Problem with length of the word: ", w)
                sys.exit()
            # Stores the last letter in an array.
            reconstruct.append(w[p-n])
        
        if len(reconstruct) % p != 0:
            print("The input file need padding, there are ", len(reconstruct), " number of words in the file.")
            sys.exit()
    return reconstruct

def format(list, file, p):
    # Append the output file with the last hex letter. Add space every 2 letters.
    
    i=0
    with open(file, 'a') as f:
        for l in list:
            if i % p == 0 and i != 0:
                f.write(' ')
            f.write(l)
            i+=1
        f.close()

def getUserArg():
    # Get user input.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:l:e:", ["help", "input=", "output=", "length=", "extract="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # Save user input in variables.
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        if o in ("-i", "--input"):
            global input_file
            input_file = str(a)
            print("Input: ", input_file)
        if o in ("-o", "--output"):
            global output_file
            output_file = str(a)
            print("Output: ", a)
        if o in ("-l", "--length"):
            global length
            length = int(a)
            print("Length: ", a)
        if o in ("-e", "--extract"):
            global extract
            extract = int(a)
            print("Extract: ", a)

# Get user input argument.
getUserArg()

# Process input file.
print("Start of process")

# Create new output file.
createFile(output_file)

# Extract the last n LSB from each word the input file.
r = extractNByte(input_file, length, extract)

# Create new output file, erase previous one if it exists. Write output to file.
format(r, output_file, length)

print("End of process")
