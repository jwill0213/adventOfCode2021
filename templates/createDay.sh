#!/bin/sh

DAY=$1
TITLE=$2

TEN=10

if [ $DAY -lt 10 ]; then
    DAY="0${DAY}"
fi

mkdir ../Day_$DAY/

cp -r main.py ../Day_$DAY/main.py

touch ../Day_$DAY/README.md
touch ../Day_$DAY/input.txt

echo "# Advent Of Code 2021 Day $DAY: $TITLE\n\n## Part 1\nTBD\n\n---\n## Part 2\nTBD" > ../Day_$DAY/README.md