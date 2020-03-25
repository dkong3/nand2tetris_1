import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

root = Tk()
root.fileName = filedialog.askopenfilename (initialdir = "C:/Users/DEXINKONG/Desktop/nand2tetris\projects/06", title = "select source file", filetypes = (("asm files", "*.asm" ), ("All files", "*.*")))
filename = str(root.fileName)
print(filename)


comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}

dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

# table of symbols used in assembly code, initialized to include
# standard ones
table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

# input R# labels
for i in range(0, 16):
    label = "R" + str(i)
    table[label] = i

labelcursor =16

# remove notes and empty lines

def file_clean ():
    fsource = open(filename, "r")
    # raw = fsource.read()
    fintm = open("intermediate.txt", "w+")
    lnum = 0
    for line in fsource:
        if line[0]== "/":
            print("this line is notes")
        elif line == "\n":
            print("empty line")
        else:
            fintm.write(line)
            lnum+=1
    print("number of code lines: ", lnum)
    fsource.close()
    fintm.close()

# first pass
def fist_pass("intermediate.txt")


file_clean()




