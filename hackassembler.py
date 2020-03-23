import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

root = Tk()
root.fileName = filedialog.askopenfilename (initialdir = "C:/Users/DEXINKONG/Desktop/nand2tetris\projects/06", title = "select source file", filetypes = (("asm files", "*.asm" ), ("All files", "*.*")))
print(root.fileName)
fscource = open(root.filName)
print(fsource)

