import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

root = Tk()
root.fileName = filedialog.askopenfilename (initialdir = "C:/Users/DEXINKONG/Desktop/nand2tetris\projects/06", title = "select source file", filetypes = (("asm files", "*.asm" ), ("All files", "*.*")))
filename = str(root.fileName)
print(filename)
fsource = open(filename, "r")
# raw = fsource.read()
line0=fsource.readlines()
print(line0.strip())
fintm = open("intermediate.txt","w+")
lnum=0
for line in fsource.readlines():
    print(line.strip())
    if line[0]== "//" and line[1] == "//" :
        print("this line is notes")
    elif line == "/n" :
        print("empty line")
    else :
        fintm.write(line)
        lnum+=1
print("number of code lines: ", lnum)
fsource.close()
fintm.close()

