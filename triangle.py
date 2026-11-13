# Problem 3: Triangle
# Return 1 if any three elements can be sides of a triangle; else 0.

def solution(A):
    # Arrange possible side lengths from smallest to largest.
    numbers = sorted(A)

    # Check each group of three neighboring numbers.
    for i in range(len(numbers) - 2):
        first = numbers[i]
        second = numbers[i + 1]
        third = numbers[i + 2]

        # Positive sides make a triangle when the two shorter
        # sides together are longer than the longest side.
        if first > 0 and first + second > third:
            return 1

    # No valid triple was found.
    return 0
