#!/usr/bin/python                                                                                   
import urotest

numCombine = urotest.uro_import('numCombine')

# def fifteen(R):
    # randNum = 15942

    # R.assertTrue(numCombine.addCombine(randNum) == 21)
    # R.assertTrue(numCombine.reduceNum(randNum) == 2)
    # R.assertTrue(numCombine.multCombine(randNum) == 360)
    # R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 9)

def sevtyeight(R):
    randNum = 78431

    R.assertTrue(numCombine.addCombine(randNum) == 23)
    R.assertTrue(numCombine.reduceNum(randNum) == 6)
    R.assertTrue(numCombine.multCombine(randNum) == 672)
    R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 6)

def thrtyfour(R):
    randNum = 34560

    R.assertTrue(numCombine.addCombine(randNum) == 18)
    R.assertTrue(numCombine.reduceNum(randNum) == 8)
    R.assertTrue(numCombine.multCombine(randNum) == 0)
    R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 0)
# not 100% sure what the outcome of that last test will be

def twenty(R):
    randNum = 20294

    R.assertTrue(numCombine.addCombine(randNum) == 17)
    R.assertTrue(numCombine.reduceNum(randNum) == 7)
    R.assertTrue(numCombine.multCombine(randNum) == 0)
    R.assertTrue(numCombine.reduceNum(numCombine.multCombine(randNum)) == 0)
