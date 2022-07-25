#!/bin/bash
if [ "$#" -lt 1 ]; then
    echo not good
    exit 1
fi
for file in $(find "$1" -type l)
do
    if [ -L "$file" ] && [ ! -e "$file" ]; then
        echo "$file"
    fi
done

