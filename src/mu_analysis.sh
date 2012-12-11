#!/usr/bin/bash

# if [ $# -lt 2 ] 
  # then
    # echo "usage: mu_analysis.sh <target src> <test source>"
    # exit 1
# fi
    
# if ![ -e mutants ] 
  # then
    # mutator.py $1
# fi

# copy the test script to mutants
# this is what we will run

pkg=$(cut -d'.' -f1 $1)

cp $2 mutants

for i in $(ls mutants/mutant*.py); do

    # Make this mutant look like the package
    mv $i mutants/$1

    cd mutants
    uroborus -s $2
    cd ..
    
    #generate the report, specific to the mutated line number
    mv mutants/$1 $i
    n=$(echo $i | tr -d [:alpha:][:punct:])
    line=$(grep ^$n mutants/mutants.txt | awk '{print $2}')
    echo "LINE:" $line
    java DisplayResult $pkg $line

done

# Take the average of PACKAGE_colors.txt

cat $pkg"_colors.txt" | awk '{s1+=$1;s2+=$2;l++}END{print s1/l"\t"s2/l}'   
