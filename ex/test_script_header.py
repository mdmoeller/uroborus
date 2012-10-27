#!/usr/bin/python

# Replace MODULE with the module you want to test
import MODULE_instrumented as MODULE

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("MODULE_passfail.txt")
MODULE.R = R


# Run tests!
