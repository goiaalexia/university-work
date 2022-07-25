#!/bin/bash
for user in $(who | awk '{ print $1 }'| uniq); do
    process=$(ps -af | grep -E -c "^${user}")
    name=$(cat /etc/passwd | grep -E "^${user}" | awk -F ':' '{print $5}')
    echo "$name $process"
done

