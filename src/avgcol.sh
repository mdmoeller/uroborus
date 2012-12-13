#!/usr/bin/bash

#usage: avgcol.sh <report file> <bug line number>
sum=0
count=0
for i in $(grep span\ id= $1 | cut -f6 -d\" | sed "s/-1//"); do
    # echo $i
    if [ $i !=  "" ]; then
        sum=$(($sum + $i))
        count=$(($count + 1))
    fi
done

# echo "END"

bug=$( grep span\ id=\"$2\" $1 | cut -f6 -d\" )

if [ $bug -lt 0 ]; then
    exit
fi

sum=$(($sum - $bug))

count=$(($count - 1))


perl -e "print "$sum/$count

echo -e '\t'$bug
