# Use class to interpret symbolic language

# file cleaning
def file_cleaning(filename):
    fsource = open(filename, "r")
    fintm = open("intermediate.txt", "w+")
    lnum = 0
    for line in fsource:
        if line[0] == "/":
            print("this line is notes")
        elif line == "\n":
            print("empty line")
        else:
            fintm.write(line)
            lnum += 1
    print("number of code lines: ", lnum)
    fsource.close()
    fintm.close()
    return fintm