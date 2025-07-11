function printRhombus(size) {
    if (size <= 0 || !Number.isInteger(size)) {
	console.log("Size must be a positive integer.");
	return;
    }

    for (let i = 1; i <= size; i++) {
	let spaces = " ".repeat(size - i);
	let stars = "*".repeat(2 * i - 1);
	console.log(spaces + stars);
    }

    for (let i = size - 1; i >= 1; i--) {
	let spaces = " ".repeat(size - i);
	let stars = "*".repeat(2 * i - 1);
	console.log(spaces + stars);
    }
}

// Example usage:
printRhombus(5);
