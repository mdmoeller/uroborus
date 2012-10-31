#!/usr/bin/python


# author: Dan Klein
# modified: Mark Moeller 24 Oct.
# modified: Samarth Kishore 10/30/2012
# modified: Mark 31 Oct.

import re, sys



# This function decides whether 'line' is the start of a new block. It returns one of 3 values:
#   returns True if this line is a def blockhead
#   returns False if this line is something else
def isNonDefBlockHead(line):

    # Not a blockhead
    if ':' not in line:
        return False

    line_end = line.split(':')[-1].strip()

    # This means it is a block:
    if line_end == '' or line_end[0] == '#':
        if len(line.strip()) > 3 and line.strip()[:3] == "def":
            return False # is a def
        else:
            return True # is a non-def blockhead!

    # Just happens to have a colon in it. Not a blockhead.
    return False


# We'll use indentLevel to help determine which lines need to be instrumented
# In particular, we use it make classes work:
#     if there is a class def on the baseline, then we shouldn't instrument level 1 as long
#     as we are inside that class, etc.
def indentLevel(line):
    """Returns an int >= 0 how far indented this line is if it has non-comment contents, or -1 for whitespace or comment"""
    
    # Whitespace or total comment
    if line.strip() == "" or line.strip()[0] == '#':
        return -1

    # If we are using tab indentation
    if line[0] == '\t': 
        count = 1
        while line[count] == '\t':
            count += 1

    # Space indentation (this will go Array-OOB if the input is not valid python)
    elif line[0] == ' ':
        count = 1
        while line[count*4] == ' ':
            count += 1

    # NO indentation, meaning it is baseline
    else:
        return 0

    return count

def coupleLine(line, lineNum, do_not_instrument_lvl = 0):

    current_level = indentLevel(line)
    block = isNonDefBlockHead(line)

    # DEBUGGING:
    # print "[dni: ", do_not_instrument_lvl, "] [level: ", current_level, "]", "[block: ", block, "]",  line

    # If we are already instrumenting, keep instrumenting
    if current_level > do_not_instrument_lvl:
        newDNILvl = do_not_instrument_lvl

    # Comment or whitespace
    elif current_level == -1:
        return ("", do_not_instrument_lvl)

    # We need to see if this is a new block, and we can start instrumenting
    elif current_level == do_not_instrument_lvl:

        # Non-def block
        if block:
            return('\n' + line, do_not_instrument_lvl + 1)

        return('\n' + line, do_not_instrument_lvl)

    # We have returned from a higher level, do not instrument at this level.
    # This is what ignores and removes comments and spaces.
    else:
        if block:
            return('\n' + line, current_level + 1)
        return ('\n' + line, current_level)
    

    # Finally, this is where we instrument:

    # Special case for "else" statements
    # NOTE: This assumes no statements in-line the else clause, which is technically valid python,
    #     but considered bad style, so we will not accept it for now.
    if line.strip() == "else:": 
        return ("\n" + line, newDNILvl)

    # grabs all of the tabs associated with the line via regex
    spaces = re.findall(r'^\s*', line)

    # prefixes the line insertion with tabs, then generates the rest of the line information
    header = "\n" + spaces[0] + "f.write(str(" + str(lineNum+1) + ") + \'\\t\' + str(R.getRunNum()) + \'\\n\')"
    header += "\n" + line

    return  (header, newDNILvl)

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

    # do not instrument level
    dni_level = 0 

    # for loop injects the instrumenting lines into the old source code
    for i in range (len(lines)):
    #instrument a file write only if it is a new statement (not a continuation)
        
        if x==0 and flag==0: 
            couple = coupleLine(lines[i], i, do_not_instrument_lvl = dni_level)
            newSource = newSource + couple[0]
            dni_level = couple[1]

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
                x = x + 1
            if (lines[i][j]==")" or lines[i][j]=="}" or lines[i][j]=="]" ):
                x = x - 1

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
