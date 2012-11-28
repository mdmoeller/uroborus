#!/usr/bin/python

import hello_instrumented as hello
target_module = hello

def testFun(runtime):
    funResult = hello.fun()

    runtime.assertTrue( 0 == funResult ) # should pass


def testSix(runtime):
    sixResult = hello.six()  

    runtime.assertTrue( 6 == sixResult ) # should fail
