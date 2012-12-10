#!/usr/bin/python

# Author: Dan Klein
# Date: 7 November 12
# Purpose: A rough, crude, amateur python code mutator

import sys
from subprocess import call

arithChars = ['+', '-', '*', '/', '%']
augAssignChars = ['+=', '-=', '*=', '/=', '%=']
numCompareChars = ['<', '>', '<=', '>=']
boolResultChars = ['True', 'False']
boolCompareChars = ['or', 'and']
eqCompareChars = ['==', '!=']

ops = [arithChars, augAssignChars, numCompareChars, boolResultChars, boolCompareChars, eqCompareChars]

def hasBool(line):
    
    # to-do: refactor this mess
    andSplits = line.split(" and ")
    orSplits = line.split(" or ")
    LTSplits = line.split("<")
    GTSplits = line.split(">")
    eqSplits = line.split("==")
    LTESplits = line.split("<=")
    GTESplits = line.split(">=")
    uneqSplits = line.split("!=")
    trueSplits = line.split("True")
    falseSplits = line.split("False")
    
    if(len(andSplits) != 1 or
       len(orSplits) != 1 or
       len(LTSplits) != 1 or
       len(GTSplits) != 1 or
       len(eqSplits) != 1 or
       len(LTESplits) != 1 or
       len(GTESplits) != 1 or
       len(uneqSplits) != 1 or
       len(trueSplits) != 1 or
       len(falseSplits) != 1):
        return True
    else:
        return False

def hasArith(line):
    
    plusSplits = line.split(" + ")
    minusSplits = line.split(" - ")
    multiSplits = line.split(" * ")
    divSplits = line.split(" / ")
    modSplits = line.split(" % ")
    
    if(len(plusSplits) != 1 or
       len(minusSplits) != 1 or
       len(multiSplits) != 1 or
       len(divSplits) != 1 or
       len(modSplits) != 1):
        return True
    else:
        return False


def hasAdjustedAssign(line):
    
    plusSplits = line.split("+=")
    minusSplits = line.split("-=")
    multiSplits = line.split("*=")
    divSplits = line.split("/=")
    modSplits = line.split("%=")

    if(len(plusSplits) != 1 or
       len(minusSplits) != 1 or
       len(multiSplits) != 1 or
       len(divSplits) != 1 or
       len(modSplits) != 1):
        return True
    else:
        return False

def isMutatable(line):
    
    if(hasBool(line) or hasArith(line) or
       hasAdjustedAssign(line)):
        return True
    else:
        return False
###
#
# THIS ALLL NEEDS CONSOLIDATION BADLY
#
###

# Mutates a line from the source, replacing the specified
# operator with the other arithmatic operators
def mutateArith(line,op):
    
    # splits the line into pieces that flank the operator
    splits = line.split(" " + op + " ")
    
    # the number of times the operator appears
    instances = len(splits) - 1
     
    # stores the mutated lines
    out = []
    
    # go over each split and change the one operator, creating 4
    # new lines per occurance of the targetted operator
    for x in range (0, len(arithChars)):
        if(arithChars[x] != op):
            
            # generates a mutation for each instance of the operator
            # in the line
            for y in range (1, instances + 1):
                out.append(mutateLineAt(splits, y, op,  arithChars[x]))
    
    return out

def mutateAugAssign(line,op):
    
    # splits the line into pieces that flank the operator
    splits = line.split(" " + op + " ")
    
    # the number of times the operator appears
    instances = len(splits) - 1
     
    # stores the mutated lines
    out = []
    
    # go over each split and change the one operator, creating 4
    # new lines per occurance of the targetted operator
    for x in range (0, len(arithChars)):
        if((augAssignChars[x]) != op):
            
            # generates a mutation for each instance of the operator
            # in the line
            for y in range (1, instances + 1):
                out.append(mutateLineAt(splits, y, op,  augAssignChars[x]))
    
    return out

def mutateCompare(line, op):
    
    splits = line.split(" " + op + " ")
    
    instances = len(splits) - 1
    
    out = []
    
    for x in range (0, len(compareChars)):
        if(compareChars[x] != op):
            for y in range (1, instances + 1):
                out.append(mutateLineAt(splits, y, op, compareChars[x]))
                
    return out

def mutateBoolCompare(line, op):
    
    splits = line.split(" " + op + " ")
    
    instances = len(splits) - 1
    
    out = []
    
    for x in range (0, len(boolCompareChars)):
        if(boolCompareChars[x] != op):
            for y in range (1, instances + 1):
                out.append(mutateLineAt(splits, y, op, boolCompareChars[x]))
                
    return out

def mutateBoolResult(line, op):
    
    splits = line.split(" " + op + " ")
    
    instances = len(splits) - 1
    
    out = []
    
    for x in range (0, len(boolCompareChars)):
        if(boolResultChars[x] != op):
            for y in range (1, instances + 1):
                out.append(mutateLineAt(splits, y, op, boolResultChars[x]))
                
    return out

def mutateEqCompare(line, op):
    
    splits = line.split(" " + op + " ")
    
    instances = len(splits) - 1
    
    out = []
    
    for x in range (0, len(boolCompareChars)):
        if(eqCompareChars[x] != op):
            for y in range (1, instances + 1):
                out.append(mutateLineAt(splits, y, op, eqCompareChars[x]))
                
    return out


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

def getNumOfInstances(line, mutOps):
    
    # stores the number of instances of each operator
    out = []
    
    for i in range (0, len(mutOps)):
        out.append(len(line.split(" " + mutOps[i] + " ")))
        
    return out

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
    
    # Counter for the total number of mutants
    mutantNumber = 0
    
    # Stores the lines of the source code
    lines = source.readlines()
    
    # iterates over the lines, keeping track of the mutatable ones
    for x in range(len(lines)):
        if(isMutatable(lines[x])):
            
            # stores the operators in the line and their instances
            mutatables = getMutatableOps(lines[x])
            instances = getNumOfInstances(lines[x], mutatables)
            
            # creates the mutated files for this line
            for y in range(len(mutatables)):
                
                # creates mutants per instance
                for z in range(1, instances[y]):
                    
                    # array containing possible mutant opertaotrs for the target op
                    newOps = ops[getOpType(mutatables[y])]
                    
                    #creates a mutant per operator mutation
                    for w in range(len(newOps)):
                        
                        # Duplicates aren't mutants, obviously
                        if(newOps[w] != mutatables[y]):
                            
                            # number of the mutant is stored int he file name
                            mutantName = "mutants/mutant" + str(mutantNumber) + ".py"
                            
                            # creates file to store mutated code
                            mutant = open(mutantName, 'w')
                            
                            # copies the source code
                            mutantSource = lines[:]
                            
                            # replaces source line with the copy
                            mutantSource[x] = mutateLineAt(mutantSource[x].split(" " + mutatables[y] + " "), z, 
                                                                                 mutatables[y], newOps[w])
                            
                            # write the mutated code
                            mutant.writelines(mutantSource)
                            
                            # logs the mutation
                            mutantLog.write(str(mutantNumber) + "\t" + str(x + 1) + "\t" + mutatables[y] + "\t"
                                            + newOps[w] + "\t" + str(z) + "\n")
                            
                            mutant.close()
                            
                            # bumps up the mutant ID
                            mutantNumber += 1
    
    mutantLog.close()


if(len(sys.argv) != 2):
    print "Usage: mutator.py <src>"
    sys.exit(1)

generateMutationPoints(sys.argv[1])
