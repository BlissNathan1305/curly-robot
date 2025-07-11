#!/bin/bash

# Print uppercase letters A-Z
for letter in {A..Z}; do
    echo -n "$letter "
done

echo    # New line for separation

# Print lowercase letters a-z
for letter in {a..z}; do
    echo -n "$letter "
done

echo    # Final newline
