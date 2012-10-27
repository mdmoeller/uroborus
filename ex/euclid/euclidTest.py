#!/usr/bin/python

import euclid_instrumented as euclid

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("euclid_passfail.txt")
euclid.R = R

g0 = euclid.gcd(10, 10)

R.assertTrue( g0 == 10 ) # Should be a PASS

g1 = euclid.gcd(100, 1000) 

R.assertTrue( g1 == 1000 ) # Should FAIL

g2 = euclid.gcd(17, 19)

R.assertTrue( g2 == 1 ) # Should PASS

g3 = euclid.gcd(192, 480) 

R.assertTrue( g3 == 96 ) # Should PASS
