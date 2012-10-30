# Author: Dan Klein
#
# Purpose: Testing out Instrum's ability to recognize line continuation
#
# To do: implement a method that uses the line continuation character
#
# example - var = 2 + 1 can be written as
#           var = 2 + \
#                 1


def isEqual(a,b):

    if( a >= b and
        a <= b): return True
    else:
        return False


def isSameMagnitude(a,b):

    if( pow(pow(a,2),0.5) ==
        pow(pow(b,2),0.5)): return True
    else:
        return False