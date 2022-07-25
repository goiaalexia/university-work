#!/bin/bash
for file in $(find "$1" -type f -name "*.log"); do
    if grep -E -q ".*\.log" $file; then
        sort "$file" -o "$file"
        echo sorted "$file".
    fi
done

