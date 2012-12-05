# !/usr/bin/python

# Author: Dan Klein
# Date: 7 November 12
# Purpose: A rough, crude, amateur python code mutator

arithChars = ['+', '-', '*', '/', '%']
augAssignChars = ['+=', '-=', '*=', '/=', '%=']
numCompareChars = ['<', '>', '<=', '>=']
boolResultChars = ['True', 'False']
boolCompareChars = ['or', 'and']
eqCompareChars = ['==', '!=']

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
    
    # No splits, just the rest of the line
    if(len(splits) == 1):
        return splits[0]
    
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


def generateMutationPoints(path):

    # File that handles source code extraction
    source = open(path, 'r')

    # Stores the name of the file for metadata generation.
    fileName = path[:-3]
    
    # Stores the lines of the source code
    lines = source.readlines()
    
    # initially empty array stores the mutatable lines numbers
    mutatableLines = []
    
    # iterates over the lines, keeping track of the mutatable ones
    for x in range (0, len(lines)):
        if(isMutatable(lines[x])):
            mutatableLines.append(x)
    
    
