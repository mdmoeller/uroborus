#!/usr/bin/python
import urotest

DT = urotest.uro_import('DT')


def training_error_zero(R):
    X = [[0], [2], [5], [8], [1]]
    Y = [0, 0, 0, 1, 1]
    h = DT.learned_tree(X,Y)
    R.assertTrue(h([0]) == 0)
    R.assertTrue(h([2]) == 0)
    R.assertTrue(h([5]) == 0)
    R.assertTrue(h([8]) == 1)
    R.assertTrue(h([1]) == 1)

def xor(R):
    X = [[0,0], [0,1], [1,0], [1,1]]
    Y = [    0,     1,     1,     0]
    h = DT.learned_tree(X,Y)
    
    # Should learn a square divided at 0.5:
    R.assertTrue(h([0.4, 0.4]) == 0)
    R.assertTrue(h([0.1, 0.1]) == 0)
    R.assertTrue(h([0.45, 0.55]) == 1)
    R.assertTrue(h([0.51, 0.23]) == 1)
    R.assertTrue(h([0.52, 0.73]) == 0)
    R.assertTrue(h([0.99, 1.8]) == 0)

