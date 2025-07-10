#!/bin/bash

# Define the size of the multiplication table
SIZE=10

# Print the header row
echo -n "   |"
for ((i=1; i<=$SIZE; i++))
do
    printf "%4d" $i
done
echo ""
echo "---+-------------------------------"

# Print each row of the multiplication table
for ((i=1; i<=$SIZE; i++))
do
    printf "%2d |" $i
    for ((j=1; j<=$SIZE; j++))
    do
	printf "%4d" $((i*j))
    done
    echo ""
done
