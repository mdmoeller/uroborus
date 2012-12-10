#!/usr/bin/bash

if [ $# -lt 3 ]
    echo "usage: mu_analysis.sh <target src> <test source>"
    exit 1
    
if ![ -e mutants ]
    mutator.py $1

# copy the test script to mutants
# this is what we will run
cp $2 mutants

for i in $(ls mutants/mutant*.py) do

    # Make this mutant look like the package
    mv $i mutants/$1

    uroborus mutants/$2

    mv mutants/$1 $i
