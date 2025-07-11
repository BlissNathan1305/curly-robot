#!/bin/bash

size=5  # Adjust this value to change the pentagon's size.  Keep it relatively small

# Top point
printf "%*s*\n" "$((size*2-1))" ""

# Upper sides
for ((i=1; i<size-1; i++)); do
    printf "%*s*%*s*\n" "$((size-i))" "" "$((2*i-1))" ""
done

# Base side
printf "*"
for ((i=1; i<=2*size-3; i++)); do
    printf "*"
done
printf "*\n"
