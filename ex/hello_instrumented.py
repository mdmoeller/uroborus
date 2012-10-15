#!/usr/bin/python

# Hand-instrumented by Mark

# ******************************************************************
# Notice that R is never declared, but it gets used by the instrumenation!
#
# For this example, I solved the problem of passing the Oracle to this
# instrumented code by leaving it up to the test code to set 'R' to the Oracle 
# before executing any methods. Essentially, R is a parameter to this
# module. 
# I would have liked to instrument the module-level code too (all the 
# function definitions) but that isn't possible if R isn't set until
# after the module has been imported.
# ******************************************************************


f = open("hello_coverage.txt", 'w')

def fun():
	
	f.write( str(4) + '\t' + str(R.getRunNum()) + '\n' )
	print "hello world!"

	f.write( str(5) + '\t' + str(R.getRunNum()) + '\n' )
	return 0

def six():
	
	f.write( str(8) + '\t' + str(R.getRunNum()) + '\n' )
	return 6
