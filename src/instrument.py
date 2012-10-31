#!/usr/bin/python


# author: Dan Klein
# modified: Mark Moeller 24 Oct.
# modified: Samarth Kishore 10/30/2012

import re, sys

def coupleLine(line,lineNum):
    
    # ignores (and removes!) comments and whitespace
    if(len(line.strip()) == 0 or line.strip()[0] == '#'): return ""
    # ignores function headers and else branches and instruments only imports on the baseline
    if(line[0].isspace() is bool("") or line.strip() == "else:"): return "\n" + line

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

    #initialize a stack to check line continuation
    x=0
    flag=0

    # for loop injects the instrumenting lines into the old source code
    for i in range (len(lines)):
    #instrument a file write only if it is a new statement (not a continuation)
        if x==0 and flag==0:
            newSource = newSource + coupleLine(lines[i], i)
        else: 
            newSource = newSource +  lines[i]
        
        """
        set flag to true if the last character 
        is the explicit line continuation character '\'
        """
        if (len(lines[i])>1 and lines[i][-2] == "\\"):
            flag=1
        else:
            flag=0

        """
        maintain a stack to ensure there are equal number of 
        opening-closing parenthesis/braces/bracket pairs
        """
        for j in range (len(lines[i])):
            if (lines[i][j]=="(" or lines[i][j]=="{" or lines[i][j]=="[" ):
		 x=x+1
	    if (lines[i][j]==")" or lines[i][j]=="}" or lines[i][j]=="]" ):
		 x=x-1

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
