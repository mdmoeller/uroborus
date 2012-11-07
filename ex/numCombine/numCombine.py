# Author: Dan Klein
# Date: 7 Nov 12

def hasZero(num):
    stringRep = str(num)
    for x in range (0, len(stringRep)):
        if(stringRep[x] == '0'):
            return True

    return False

def multCombine(num):
    stringRep = str(num)
    prod = 1
    for x in range (0, len(stringRep)):
        prod *= int(stringRep[x])
        
    return prod

def addCombine(num):
    stringRep = str(num)
    sum = 0
    for x in range (0, len(stringRep)):
        sum += int(stringRep[x])
        
    return sum

def reduceNum(num):
    result = 0
    if(hasZero(num)):
        result = addCombine(num)
    else:
        result = multCombine(num)
        
    if(result < 10):
        return result
    else:
        return reduceNum(result)
