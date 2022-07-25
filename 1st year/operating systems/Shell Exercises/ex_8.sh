#!/bin/bash
avg=0
count=1
touch result.txt
for file in "$@"; do
    comms=0
    if grep -Eq ".*\.txt" <<< $file; then
        input=$file
        while IFS= read -r line; do
            chars=${#line}
            let "avg=avg+chars"
            let "count=count+1"
        done < $input
    fi
    if grep -Eq ".*\.sh" <<< $file; then

        comms=0
        comms=$(grep -E -c "^#" $file)
        let "comms=comms-1"
        echo "The number of comments in $file is $comms" >> result.txt
    fi
    if grep -Eq ".*\.c" <<< $file; then
        sed -i "/^$/d" $file
        echo "Replaced the empty rows in $file" >> result.txt
    fi
done
let "avg=avg/count"
echo "The average of txt files is $avg" >> result.txt

