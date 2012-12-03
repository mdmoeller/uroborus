#!/usr/bin/python
import instrument
import importlib

import sys

def uro_import(module):

    # instrument the module
    instrument.makeInstrumFile(module + '.py')

    # return instrumented version
    instrumented = importlib.import_module(module + '_instrumented')

    # set the global so that uroborus can see it
    global target
    target = instrumented

    return instrumented
