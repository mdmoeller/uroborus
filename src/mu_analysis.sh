#!/usr/bin/bash

if [ $# -lt 2 ] 
  then
    echo "usage: mu_analysis.sh <target src> <test source>"
    exit 1
fi

pkg=$(echo $1 | cut -d'.' -f1)
    
if [ ! -e mutants ] 
  then
    echo "Mutating " $pkg "..."
    mutator.py $1
fi

# copy the test script to mutants
# this is what we will run uroborus on
# each time
cp $2 mutants

cd mutants
for i in $(ls mutant*.py); do

    rm -rf *_instrumented.py *_passfail.txt *_coverage.txt *.pyc *_report.html *_colors.txt *~

    # Make this mutant look like the package
    mv $i $1

    #generate the report, specific to the mutated line number
    n=$(echo $i | tr -d [:alpha:][:punct:])
    line=$(grep ^$n[^0-9] mutants.txt | awk '{print $2}')

    echo "Running mutant "$n" (mutated line "$line")"

    uroborus -s $2
    

    java DisplayResult $pkg

    if [ $? == 0 ]; then
        avgcol.sh $pkg"_report.html" $line >> ../$pkg"_colors.txt"
    fi

    # Fix this mutant back
    mv $1 $i
done

cd ..

# Take the average of PACKAGE_colors.txt

cat $pkg"_colors.txt" | awk '{s1+=$1;s2+=$2;l++}END{print s1/l"\t"s2/l}'   
