# Author: Dan
# Creation date: 30 October 2012
# Purpose: tests the branches file and its functions

import branches_instrumented as branches

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("branches_passfail.txt")
branches.R = R

# All of these should pass.
# This may or may not be possible. Consider it the ultimate blackbox.

R.assertTrue(branches.fun1(1,1) == 23)
R.assertTrue(branches.fun1(1,-1) == 23)
R.assertTrue(branches.fun1(-1,4) == 23)
R.assertTrue(branches.fun1(1,-4) == 23)
R.assertTrue(branches.fun1(0,1) == 23)
R.assertTrue(branches.fun1(1,0) == 23)
R.assertTrue(branches.fun1(-4, -4) == 23)

R.assertTrue(branches.fun2(1,1,1) == 3)
R.assertTrue(branches.fun2(1,-1,1) == 3)
R.assertTrue(branches.fun2(1,1,-1) == 5)
R.assertTrue(branches.fun2(-1,-1,1) == 0)
R.assertTrue(branches.fun2(-1,1,-1) == 4)
R.assertTrue(branches.fun2(1,-1,-1) == 15)
R.assertTrue(branches.fun2(-1,-1,-1) == 1)