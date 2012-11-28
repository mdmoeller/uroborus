# !/usr/bin/python

# Author: Dan Klein
# Date: 7 November 12
# Purpose: A rough, crude, amateur python code mutator

arithChars = ['+', '-', '*', '/', '%']

def hasBool(line):
    
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

# Mutates a line from the source, replacing the specified
# operator with the other arithmatic operators
def mutateArith(line,op):
    
    # splits the line into pieces that flank the operator
    splits = line.split(" " + op + " ")
    
    # stores the mutated lines
    out = []
    
    # go over each split and change the one operator, creating 4
    # new lines per occurance of the targetted operator
    
    return out

# Recursive function that takes goes over the current split
# of the line, replacing the target instance of the operator
# with the new operator
def mutateLineAt(splits, instanceNum, targetOp, replaceOp):
    
    if(len(splits) == 1):
        return splits[0]
    
    if(instanceNum == 0):
        return splits[0] + " " + targetOp + " " +  mutateLineAt(splits[1:], 0, \
                                                                    targetOp, \
                                                                    replaceOp)
    
    if(instanceNum == 1):
        return splits[0] + " " + replaceOp + " " +  mutateLineAt(splits[1:], 0, \
                                                                    targetOp, \
                                                                    replaceOp)
    
    return splits[0] + " " + targetOp + " " +  mutateLineAt(splits[1:], instanceNum-1,\
                                                                targetOp, replaceOp)


