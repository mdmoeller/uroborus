#!/usr/bin/python


# author: Dan Klein
# modified: Mark Moeller 24 Oct.

import re, sys

def coupleLine(line, lineNum):

    # ignores (and removes!) comments and whitespace
    if(len(line.strip()) == 0 or line[0] == '#'): return ""

    # ignores function headers and else branches
    if(line[:3] == "def" or line.strip() == "else:"): return "\n" + line

    # grabs all of the tabs associated with the line via regex
    spaces = re.findall(r'^\s*', line)

    # prefixes the line insertion with tabs, then generates the rest of the line information
    header = "\n" + spaces[0] + "f.write(str(" + str(lineNum+1) + ") + \'\\t\' + str(R.getRunNum()) + \'\\n\')"
    header += "\n" + line

    return  header

def makeInstrumFile(path):

    # File that handles source code extraction
    f1 = open(path, 'r')

    # Stores the name of the file for metadata generation. Local files only, please.
    fileName = path[:-3]

    # String that stores the instrumented source code
    newSource = "f = open(\"" + fileName + "_coverage.txt\", \'w\')\n"

    # Reads in each line into an array
    lines = f1.readlines()

    # for loop injects the instrumenting lines into the old source code
    for x in range (0, len(lines)):
        newSource = newSource + coupleLine(lines[x], x)

    # initializes and writes the instrumented code
    newFile = open( fileName + "_instrumented.py", 'w')
    newFile.write(newSource)
    newFile.close()
    f1.close()

def main():
    args = sys.argv
    if len(args) != 2:
        print "usage: Instrum.py <source filename>"
        sys.exit(1)

    makeInstrumFile(args[1])

main()
