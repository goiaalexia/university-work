#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Not enough arguments!"
    exit 1
fi

for dir in $@; do

    if [ -d $dir ]; then
        files=$(ls -l $dir | awk {'print $9'})
        for file in $files; do
            if grep -Eq ".*\.txt" <<< $file; then
                echo $file >> result2.txt
            fi

            if grep -Eq ".*\.sh" <<< $file; then
                sed -i '/^$/d' $file
                echo "deleted empty lines from $file" >> result2.txt
            fi

            if grep -Eq ".*\.exe" <<< $file; then
                bytes=$(wc -c $file | awk {'print $1'})
                echo "File $file has $bytes bytes"  >> result2.txt
            fi



        done
    fi

done

