#!/usr/bin/python

__author__ = 'Dan'

import multiLineArgs_instrumented as multiLineArgs

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("multiLineArgs_passfail.txt")
multiLineArgs.R = R

R.assertTrue( multiLineArgs.isEqual(3, 3) ) # Should pass
R.assertTrue( multiLineArgs.isEqual(3, 4) ) # Should fail

R.assertTrue( multiLineArgs.isSameMagnitude(3, -3) ) # should pass
R.assertTrue( multiLineArgs.isSameMagnitude(3, 3) )  # should pass
R.assertTrue( multiLineArgs.isSameMagnitude(4, -3) ) # should fail
R.assertTrue( multiLineArgs.isSameMagnitude(3, 4) )  # should fail

m1 = multiLineArgs.mean(2, 2, 3, 3); # should be 2.5
m2 = multiLineArgs.mean(2, 3, 3, 4); # should be 3.0

s1 = multiLineArgs.stringConcat("This ", "is ", "a test.")  # Should be "This is a test"
s2 = multiLineArgs.stringConcat("ML", "ALG", "SE")          # Should be "MLALGSE"

R.assertTrue( m1 == 2.50 )  # should pass
R.assertTrue( m2 == 3.01 )  # should fail

R.assertTrue( s1 is "This is a test.")  # should pass
R.assertTrue( s2 is "mlalgse")          # should fail

