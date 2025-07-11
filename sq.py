def print_square(size):
  """Prints a square of asterisks with the given size."""

  if not isinstance(size, int):
    raise TypeError("size must be an integer")
  if size < 0:
    raise ValueError("size must be >= 0")

  for _ in range(size):
    print("*" * size)

# Example usage:
size = 5
print_square(size)
