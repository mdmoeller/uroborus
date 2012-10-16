#!/usr/bin/python

def gcd( a, b ):

	big = max(a,b)
	small = min(a,b)

	r = big - small
	
	if r == 0:
		return small
	else:
		return gcd(small, r)
