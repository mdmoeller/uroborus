#!/usr/bin/python

# Author: Dan Klein
# Creation date: 7 November 2012
# Freeze date: 12 December 2012
# Purpose: Python code mutation generation

import sys
from subprocess import call

# These arrays store all of the mutatable operators the mutator can mutate.
#
# They're grouped by their interchangability; that is, any operator in a 
# given array can be replaced by any other operator in that array and still
# be valid in most cases.

arithChars = ['+', '-', '*', '/', '%']
augAssignChars = ['+=', '-=', '*=', '/=', '%=']
numCompareChars = ['<', '>', '<=', '>=']
boolResultChars = ['True', 'False']
boolCompareChars = ['or', 'and']
eqCompareChars = ['==', '!=']

# Stores the operator arrays so that they can be accessed programmatically
ops = [arithChars, augAssignChars, numCompareChars, boolResultChars, boolCompareChars, eqCompareChars]

# Returns true if there are mutatable operators in the given line of code
def isMutatable(line):
    
    # True if line contains mutatable operators
    if(getMutatableOps(line) != []):
        return True
    else:
        return False

# Recursive function that takes goes over the current split
# of the line, replacing the target instance of the operator
# with the new operator
def mutateLineAt(splits, instanceNum, targetOp, replaceOp):
    
    # No splits, just the rest of the line and a comment noting the mutation
    if(len(splits) == 1):
        return splits[0][:-1] + " # THIS LINE HAS BEEN MUTATED\n"
    
    # Replacement has occurred, returning the rest of the line as is
    if(instanceNum == 0):
        return splits[0] + " " + targetOp + " " +  mutateLineAt(splits[1:], 0, \
                                                                    targetOp, \
                                                                    replaceOp)
    
    # At the replacement instance, replace target operator with new operator.
    if(instanceNum == 1):
        return splits[0] + " " + replaceOp + " " +  mutateLineAt(splits[1:], 0, \
                                                                    targetOp, \
                                                                    replaceOp)
    
    # Count down until the operator we wish to replace is reached
    return splits[0] + " " + targetOp + " " +  mutateLineAt(splits[1:], instanceNum-1,\
                                                                targetOp, replaceOp) 


def getOpType(op):
    
    # checks to see which array the op is in
    for i in range (0, len(ops)):
        if(op in ops[i]):
            return i
    
    # if we get here, we got problems
    return -1

def getMutatableOps(line):
    
    # Holds the mutatable operators in a given line
    out = []
    
    # Goes into each array of operators, splitting the line on each
    for i in range (0, len(ops)):
        
        for j in range (0, len(ops[i])):
            
            # splits the line on the operator
            splits = line.split(" " + ops[i][j] + " ")
            
            if(len(splits) > 1):
                
                # appends the operator to the output if there is more than one split
                out.append(ops[i][j])
    
    return out

# Returns the number of times each operator occurs in the line
def getNumOfInstances(line, mutOps):
    
    # stores the number of instances of each operator
    out = []
    
    for i in range (0, len(mutOps)):
        
        # Stores the number of times an operator is found in a given line
        out.append(len(line.split(" " + mutOps[i] + " ")))
        
    return out

# Generates and writes mutated versions of Python source code located at the specified path
def generateMutationPoints(path):

    # File that handles source code extraction
    source = open(path, 'r')
    
    # creates directory to store mutated code
    call(["mkdir", "-p", "mutants"])
    call("rm -f mutants/*", shell = True)
    
    # File that logs all of the mutations
    mutantLog = open("mutants/mutants.txt", 'w')

    # Stores the name of the file for metadata generation.
    fileName = path[:-3]
    
    # Mutant "ID number" for file names
    mutantNumber = 0
    
    # Stores the lines of the source code
    lines = source.readlines()
    
    # iterates over the lines, keeping track of the mutatable ones
    for lineNum in range(len(lines)):
        if(isMutatable(lines[lineNum])):
            
            # stores the operators that appear in the line and their instances
            mutatables = getMutatableOps(lines[lineNum])
            instances = getNumOfInstances(lines[lineNum], mutatables)
            
            # creates the mutated files for this operator
            for opNum in range(len(mutatables)):
                
                # creates mutants per instance
                for instance in range(1, instances[opNum]):
                    
                    # array containing possible mutant opertaotrs for the target op
                    newOps = ops[getOpType(mutatables[opNum])]
                    
                    #creates a mutant per operator mutation
                    for newOpNum in range(len(newOps)):
                        
                        # Duplicates aren't mutants, obviously
                        if(newOps[newOpNum] != mutatables[opNum]):
                            
                            # number of the mutant is stored int he file name
                            mutantName = "mutants/mutant" + str(mutantNumber) + ".py"
                            
                            # creates file to store mutated code
                            mutant = open(mutantName, 'w')
                            
                            # copies the source code
                            mutantSource = lines[:]
                            
                            # replaces source line with the copy
                            mutantSource[lineNum] = mutateLineAt(mutantSource[lineNum].split(" " + mutatables[opNum] + " "), 
                                                                 instance, mutatables[opNum], newOps[newOpNum])
                            
                            # write the mutated code
                            mutant.writelines(mutantSource)
                            
                            # logs the mutation
                            mutantLog.write(str(mutantNumber) + "\t" + str(lineNum + 1) + "\t" + mutatables[opNum] + "\t"
                                            + newOps[newOpNum] + "\t" + str(instance) + "\n")
                            
                            mutant.close()
                            
                            # bumps up the mutant ID
                            mutantNumber += 1
    
    mutantLog.close()


if(len(sys.argv) != 2):
    print "Usage: mutator.py <src>"
    sys.exit(1)

generateMutationPoints(sys.argv[1])
