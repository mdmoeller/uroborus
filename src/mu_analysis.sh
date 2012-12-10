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

    uroborus -s mutants/$2
    
    #generate the report, specific to the mutated line number
    # --HERE--

    mv mutants/$1 $i
    n=$(echo $i | tr -d [:alpha:][:punct:])
    line=$(grep "^"$n mutants/mutants.txt | awk '{print $2}')
    java DisplayResult mutants $line

# Take the average of PACKAGE_colors.txt
    cat color.txt | awk '{s1+=$1;s2+=$2;l++}END{print s1/l"\t"s2/l}'   
