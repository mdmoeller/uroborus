# Author: Dan
# Creation date: 30 October 2012
# Purpose: tests the branches file and its functions

import branches_instrumented as branches
target_module = branches

# All of these should pass.
# This may or may not be possible. Consider it the ultimate blackbox.

def t0(R):
    R.assertTrue(branches.fun1(1,1) == 18)

def t1(R):
    R.assertTrue(branches.fun1(1,-1) == 23)

def t2(R):
    R.assertTrue(branches.fun1(-1,4) == 23)

def t3(R):
    R.assertTrue(branches.fun1(1,-4) == 23)

def t4(R):
    R.assertTrue(branches.fun1(0,1) == 18)

def t5(R):
    R.assertTrue(branches.fun1(1,0) == -9)

def t6(R):
    R.assertTrue(branches.fun1(-4, -4) == 45)


def t7(R):
    R.assertTrue(branches.fun2(1,1,1) == 3)

def t8(R):
    R.assertTrue(branches.fun2(1,-1,1) == 0)

def t9(R):
    R.assertTrue(branches.fun2(1,1,-1) == -2)

def t10(R):
    R.assertTrue(branches.fun2(-1,-1,1) == 3)

def t11(R):
    R.assertTrue(branches.fun2(-1,1,-1) == -4)

def t12(R):
    R.assertTrue(branches.fun2(1,-1,-1) == 0)

def t13(R):
    R.assertTrue(branches.fun2(-1,-1,-1) == -2)

def t14(R):
    R.assertTrue(branches.fun2(-10,3,-1) == -37)

def t15(R):
    R.assertTrue(branches.fun2(3, 2, -5) == -11)

def t16(R):
    R.assertTrue(branches.fun2(3,17,4) == 20)

def t17(R):
    R.assertTrue(branches.fun2(2,3,5) == 7)
