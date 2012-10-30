#!/usr/bin/python

import DT_instrumented as DT

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("DT_passfail.txt")
DT.R = R

X = [[0], [2], [5], [8], [1]]
Y = [0, 0, 0, 1, 1]
h = DT.learned_tree(X,Y)

R.assertTrue( h([0]) == 0 )

R.assertTrue( h([5]) == 0 )

R.assertTrue( h([7.9]) == 1 )

R.assertTrue( h([20]) == 1 )
