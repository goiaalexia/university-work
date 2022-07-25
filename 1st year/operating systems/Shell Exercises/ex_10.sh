#!/bin/bash

touch sol.txt

echo Input N1:

read N1

[ "$N1" -eq "$N1" ] 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Wrong input!"
    exit 1
fi

while true; do
    echo Filename:
    read filename

    if grep -Eq ".*\.txt" <<< $filename; then
        count=$(wc -l $filename|awk {'print $1'})
        if [ "$count" -eq "$N1" ]; then
            echo $filename >> sol.txt
        fi
    fi

    if [[ "$filename" == "stop" ]]; then
        break
    fi
done

echo "Content of file:"
cat sol.txt

