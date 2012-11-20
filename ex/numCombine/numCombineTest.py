#!/usr/bin/python                                                                                   

import numCombine_instrumented as numCombine

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("numCombine_passfail.txt")
numCombine.R = R

randNum = 15942

R.assertTrue(numCombine.addCombine(randNum) == 21)
R.assertTrue(numCombine.reduceNum(randNum) == 2)
R.assertTrue(numCombine.multCombine(randNum) == 360)
R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 9)

randNum = 78431

R.assertTrue(numCombine.addCombine(randNum) == 23)
R.assertTrue(numCombine.reduceNum(randNum) == 6)
R.assertTrue(numCombine.multCombine(randNum) == 672)
R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 6)

randNum = 34560

R.assertTrue(numCombine.addCombine(randNum) == 18)
R.assertTrue(numCombine.reduceNum(randNum) == 8)
R.assertTrue(numCombine.multCombine(randNum) == 0)
R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 0)
# not 100% sure what the outcome of that last test will be

randNum = 20294

R.assertTrue(numCombine.addCombine(randNum) == 17)
R.assertTrue(numCombine.reduceNum(randNum) == 7)
R.assertTrue(numCombine.multCombine(randNum) == 0)
R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 0)
