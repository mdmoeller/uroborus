# Author: Dan
# Creation date: 31 October 2012
# Purpose: Does a system of needlessly complicated if checks

def fun1(a,b):

    m = (3 * a) + b
    if(m >= 0 ):

          m = a * b
          a = b + 2

          if(m * (b + a) < 0):

              #shouldn't ever get here (right?)
              a = m - 3
              b = a + m

          else:

              m = 3
              b = a * 5

          return m + b

    else:
          m *= -3
          a = b + 2
          if(m < 0):
              return m
          else:
              return a

def fun2(a, b, c):

    n = (a + c) * (-b)

    if(n < 0):

        if( a > c):

            b = a - c
            n += b

            return n

        n = a + 4

        b = 2 * c

        return n - b

    a = n + b

    c += -a

    return c
