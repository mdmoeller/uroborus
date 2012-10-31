# Author: Dan
# Creation date: 30 October 2012
# Purpose: parses sentence into an array of string containing its words

def spaceCounter(line):

    # this should be 0, "whoops"
    count = 1;

    for x in range(0, len(line)):
        if(line[x] == ' ' and x != 0):
            count += 1

    return count

def firstWord(line):

    finishIndex = 0;

    for x in range (0, len(line)):
        if(line[x] != ' '):
            finishIndex += 1
        else:
            break

    return line[:finishIndex]

def firstSpace(line):

    for x in range (0, len(line)):
        if(line[x] == " "):
            # should just be x
            return x+1

    return -1


def wordsFromSentence(line):

    out = [""] * (spaceCounter(line) + 1)
    dupe = line
    i = 0

    while(True):
        out[i] = firstWord(dupe)
        if(firstSpace(dupe) == -1):
            break
        else:
            dupe = dupe[firstSpace(dupe)+1:len(dupe)]
            i += 1


    return out
