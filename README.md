#Steganography LSB extractor tool

## Presentation

Author: OurBinariArc
Project: CTF
Program: stego.py
Version: 1.0
Date: 15-Aug-2022

## Program description
This script extracts the last n LSB of a hex or binary file and combines them into an output file.

## Usage
stego.py -i input_file -o output_file -l length -e extract_bit
-i --input        - Input file
-o --output       - Output file
-l --length       - Length of the words in input file (2 for hex file, 8 for binary file), must be separated by space
-e --extract      - number of Least Significant Bit (LSB) to extract from the words

Examples:
python3 stego.py -i input.bin -o output.bin -l 8 -e 2
python3 stego.py -i input.hex -o output.hex -l 2 -e 1
