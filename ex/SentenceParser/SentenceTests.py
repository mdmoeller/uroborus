#!/usr/bin/python

# Author: Dan
# Creation date: 30 October 2012
# Purpose: tests the SentenceParser class and its functions

import SentenceParser_instrumented as SentenceParser

from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("SentenceParser_passfail.txt")
SentenceParser.R = R

string = "Hello, world."

# these should all pass

R.assertTrue(SentenceParser.spaceCounter(string) == 1)
R.assertTrue(SentenceParser.firstSpace(string) == 6)
R.assertTrue(SentenceParser.firstWord(string) == "Hello,")

parses = SentenceParser.wordsFromSentence(string)

R.assertTrue(parses[0] == SentenceParser.firstWord(string))
R.assertTrue(parses[1] == "world.")
