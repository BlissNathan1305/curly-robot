#!/bin/bash

height=5  # Adjust this value to change the pyramid's height

for ((i=1; i<=height; i++)); do
    # Calculate spaces before the stars
    spaces=$((height - i))

    # Print spaces
    for ((j=1; j<=spaces; j++)); do
	printf " "
    done

    # Calculate the number of stars (odd numbers)
    stars=$((2 * i - 1))

    # Print stars
    for ((k=1; k<=stars; k++)); do
	printf "*"
    done

    # Print a newline to move to the next row
    echo ""
    done
