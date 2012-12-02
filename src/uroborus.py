#!/usr/bin/python

import sys
import os
import types
import importlib
import traceback
from RuntimeOracle import RuntimeOracle

sys.path.append(os.getcwd())

args = sys.argv

# Define terminal colors:
red = '\033[0;31m'
green = '\033[0;32m'
reset = '\033[0;0m'
brown = '\033[0;33m'

# Wrong number of args: Complain and quit
if len(args) != 2:
    sys.stderr.write("Usage: uroborus.py <test case file>\n")
    sys.exit(1)

test_module_filename = args[1]
test_module_name = ''.join(test_module_filename.split('.')[:-1])


# Place UROBORUS test module constraints here.
for line in open(test_module_filename, 'r').readlines():

    # Constraint on importing from ... *
    if line.strip()[:4] == "from" and line.strip()[-1:] == "*":
        sys.stderr.write('uroborus: "from ... import *" statements are not allowed in Uroborus tests. Packages must be imported and used by name.\n')
        sys.exit(2)


# Import the test script or complain and quit
try:
    test_module = importlib.import_module(test_module_name)
except ImportError as ie:
    sys.stderr.write("urobourus: Trouble importing test module: " + test_module_name + '\n')
    sys.stderr.write(red + str(ie) + reset + '\n')
    sys.stderr.write('\n' + str(sys.exc_info()[0]) + '\n')
    raise
except Exception as e:
    sys.stderr.write("uroborus: Unexpected error while trying to import test module. Exiting.\n")
    sys.stderr.write(red + str(e) + reset + '\n')
    raise

# Now prepare to run the tests
try:
    target_module = test_module.target_module
    passfail_filename = ''.join(target_module.__name__.split('_')[:-1]) + "_passfail.txt"
    RO = RuntimeOracle(passfail_filename)
    target_module.R = RO
except:
    sys.stderr.write("uroborus: Test module must define which module is being tested by setting a 'target_module' variable\n")
    sys.exit(4)


attributes = dir(test_module)

# Compute the longest attribute name for pretty printing
longest = 0
for attr in attributes:
    if len(attr) > longest:
        longest = len(attr)

# If there is an init method, call it first and remove it:
if "init" in attributes:
    init = getattr(test_module, "init")
    if type(init) is types.FunctionType:
        try:
            init(RO)
            run_passed = RO.run_complete()
            print green if run_passed else red,
            print init + " "*(longest - 2),
            print "PASS" if run_passed else "FAIL",
            print reset
        except:
            print "uroborus: Could not run tests; init method crashed."
            raise
        attributes.remove("init")


print "\n\nTest cases:"

# Run all the methods in the test module
for attr in attributes:
    obj = getattr(test_module, attr)
    if type(obj) is types.FunctionType:
        try:
            obj(RO)
            run_passed = RO.run_complete()
            print green if run_passed else red,
            print attr + " "*(longest + 2 - len(attr)),
            print "PASS" if run_passed else "FAIL",
            print reset
        except Exception as e:
            RO.except_fail()
            print red,
            print attr + " "*(longest + 2 - len(attr)),
            print "CRASH/FAIL",
            print brown + '(' + str(e) + ')' + reset

print '\n' + reset + "Testing complete."
print "Passes: " + green + str(RO.passes()) + reset 
print "Fails: " + red + str(RO.fails()) + '\n\n' + reset
