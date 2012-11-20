#!/usr/bin/python

import sys
import os
import types
import importlib
import traceback
from RuntimeOracle import RuntimeOracle

sys.path.append(os.getcwd())

args = sys.argv

# Wrong number of args: Complain and quit
if len(args) != 2:
    sys.stderr.write("Usage: uroborus.py <test case file>\n")
    sys.exit(1)

test_module_str = ''.join(args[1].split('.')[:-1])

# Import the test script or complain and quit
try:
    test_module = importlib.import_module(test_module_str)
except ImportError:
    sys.stderr.write("Trouble importing test module: " + test_module_str + '\n')
    sys.stderr.write('\n' + str(sys.exc_info()[0]) + '\n')
    sys.exit(2)
except:
    sys.stderr.write("Unexpected error while trying to import test module. Exiting.\n")
    sys.exit(3)

try:
    target_module = test_module.target_module
    RO = RuntimeOracle(target_module.__name__ + "_passfail.txt")
    target_module.R = RO
except:
    sys.stderr.write("Test module must define which module is being tested by setting a 'target_module' variable\n")
    sys.exit(4)

# Run all the methods in the test module
for attr in dir(test_module):
    obj = getattr(test_module, attr)
    if type(obj) is types.FunctionType:
        try:
            print obj.__name__ + ": ",
            obj(RO)
            run_passed = RO.run_complete()
            print "PASS" if run_passed else "FAIL"
        except Exception as e:
            print str(e)
            RO.except_fail()
            print "CRASH/FAIL"

print "Testing complete.\nPasses: ", RO.passes(), "\nFails: ", RO.fails()
