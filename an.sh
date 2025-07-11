#!/bin/bash

# Length of the generated code
length=12

# Generate random alphanumeric code
code=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w $length | head -n 1)

echo "Your random code: $code"
