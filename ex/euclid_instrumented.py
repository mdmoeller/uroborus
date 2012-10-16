#!/usr/bin/python

# Instrumented by hand by Mark

f = open("euclid_coverage.txt", 'w')

def gcd( a, b ):

	f.write( str(5) + '\t' + str(R.getRunNum()) +'\n' )
	big = max(a,b)
	f.write( str(6) + '\t' + str(R.getRunNum()) +'\n' )
	small = min(a,b)

	f.write( str(8) + '\t' + str(R.getRunNum()) +'\n' )
	r = big - small
	
	f.write( str(10) + '\t' + str(R.getRunNum()) +'\n' )
	if r == 0:
		f.write( str(11) + '\t' + str(R.getRunNum()) +'\n' )
		return small
	# f.write( str(12) + '\t' + str(R.getRunNum()) +'\n' )    #It would appear line 12 cannot be measured
	else:
		f.write( str(13) + '\t' + str(R.getRunNum()) +'\n' )
		return gcd(small, r)
