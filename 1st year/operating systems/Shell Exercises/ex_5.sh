#!/bin/bash
if [ "$#" -eq 0 ]; then
    echo "not good"
    exit 1
fi
while true
do
    for proc in "$@"
    do
        found=$(ps | grep -E "${proc}$")

        if [ ! -z "$found" ]; then
            pid=$(echo "$found" | awk '{print $1}')
            kill -9 "$pid"
            echo "killed $proc"
        fi
    done

    echo "waiting."
    sleep 1
done

