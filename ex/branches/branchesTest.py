# Author: Dan
# Creation date: 30 October 2012
# Purpose: tests the branches file and its functions

import branches_instrumented as branches

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("branches_passfail.txt")
branches.R = R

# All of these should pass.
# This may or may not be possible. Consider it the ultimate blackbox.

R.assertTrue(branches.fun1(1,1) == 18)
R.assertTrue(branches.fun1(1,-1) == 23)
R.assertTrue(branches.fun1(-1,4) == 23)
R.assertTrue(branches.fun1(1,-4) == 23)
R.assertTrue(branches.fun1(0,1) == 18)
R.assertTrue(branches.fun1(1,0) == -9)
R.assertTrue(branches.fun1(-4, -4) == 45)

R.assertTrue(branches.fun2(1,1,1) == 3)
R.assertTrue(branches.fun2(1,-1,1) == 0)
R.assertTrue(branches.fun2(1,1,-1) == -2)
R.assertTrue(branches.fun2(-1,-1,1) == 3)
R.assertTrue(branches.fun2(-1,1,-1) == -4)
R.assertTrue(branches.fun2(1,-1,-1) == 0)
R.assertTrue(branches.fun2(-1,-1,-1) == -2)
R.assertTrue(branches.fun2(-10,3,-1) == -37)
R.assertTrue(branches.fun2(3, 2, -5) == -11)
R.assertTrue(branches.fun2(3,17,4) == 20)
R.assertTrue(branches.fun2(2,3,5) == 7)