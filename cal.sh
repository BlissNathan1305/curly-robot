#!/bin/bash

# Function to add two numbers
add() {
    echo "scale=2; $1 + $2" | bc
}

# Function to subtract two numbers
subtract() {
    echo "scale=2; $1 - $2" | bc
}

# Function to multiply two numbers
multiply() {
    echo "scale=2; $1 * $2" | bc
}

# Function to divide two numbers
divide() {
    if [ $2 != 0 ]; then
	echo "scale=2; $1 / $2" | bc
    else
	echo "Error: Division by zero is not allowed."
    fi
}

# Main function
main() {
    echo "Simple Calculator"
    echo "1. Addition"
    echo "2. Subtraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "5. Quit"

    while true; do
	read -p "Choose an operation (1/2/3/4/5): " choice

	case $choice in
	    1)
		read -p "Enter first number: " num1
		read -p "Enter second number: " num2
		echo "Result: $(add $num1 $num2)"
		;;
	    2)
		read -p "Enter first number: " num1
		read -p "Enter second number: " num2
		echo "Result: $(subtract $num1 $num2)"
		;;
	    3)
		read -p "Enter first number: " num1
		read -p "Enter second number: " num2
		echo "Result: $(multiply $num1 $num2)"
		;;
	    4)
		read -p "Enter dividend: " num1
		read -p "Enter divisor: " num2
		echo "Result: $(divide $num1 $num2)"
		;;
	    5)
		echo "Goodbye!"
		exit 0
		;;
	    *)
		echo "Invalid choice. Please choose a valid operation."
		;;
	esac
    done
}

main
