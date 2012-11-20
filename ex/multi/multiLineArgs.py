# Author: Dan Klein
#
# Purpose: Testing out Instrum's ability to recognize line continuation



def isEqual(a,b):

    if( a >= b and
        a <= b): return True
    else:
        return False


def isSameMagnitude(a,b):

    if( pow(pow(a,
                 2),0.5) ==
                 pow(pow(b,2),0.5)): return True
    else:
        return False

def mean(a, b, c, d):

    sum = a + b + \
          c + d
    sum /= 4.0
    return sum

def stringConcat(str1, str2, str3):

    output = str1 + \
             str2 \
             + str3

    return output

