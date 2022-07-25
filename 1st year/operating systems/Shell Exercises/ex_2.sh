#!/bin/bash
n=0
cur=$(ls | awk '{print $1}')
while [ "$n" -lt 2 ]; do
    for A in $cur; do
        if grep -E -q ".*\.c" $A ; then
            if [ $(wc -l "$A" | awk {'print $1'}) -gt 500 ]; then
                let "n=n+1"
                echo $A
            fi
        fi
        if [ "$n" -eq 2 ]; then
            break
        fi
    done
    break
done

