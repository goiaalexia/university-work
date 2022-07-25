#!/bin/bash

touch files.txt

if [ "$#" -lt 1 ]; then
    echo "Provide enough arguments!"
    exit 1
fi

while true; do
    read r1
    if [[ "$r1" == "stop" ]]; then
        break
    fi

    echo "$r1" >> files.txt
done


for word in $@; do
    while IFS= read -r file; do
        cond=0
        if grep -Eq ".*${word}.*"; then
            cond=1
        fi
    done < files.txt
    if [ "$cond" -eq 0 ]; then
        echo "Word $word not found, therefore the execution will be suspended."
    fi
done

