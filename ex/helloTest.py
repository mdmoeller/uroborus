#!/usr/bin/python

import hello_instrumented as hello

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("hello_passfail.txt")

hello.R = R

funResult = hello.fun()

R.assertTrue( 0 == funResult ) # should pass

sixResult = hello.six()  

R.assertTrue( 5 == sixResult ) # should fail
