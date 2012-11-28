#!/usr/bin/python

import BPT_instrumented as BPT
# import BPT

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("BPT_passfail.txt")
BPT.R = R


import random


LIST = range(50)


for trial in range(10):

    # Tree is a new B+ tree with order 5
    tree = BPT.BPT(5)

    # Add every element in [0..49] in a random order, giving a different BPT every time
    random.shuffle(LIST)
    for el in LIST:
        tree.add(el, str(el) + "*")

    # Just make sure that the BPT finds all the right values
    for el in LIST:
        R.assertTrue(tree.search(el) == str(el) + "*")
