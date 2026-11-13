# Problem 4: AbsDistinct
# Return the number of different absolute values in A.

def solution(A):
    # Store absolute values without duplicates.
    absolute_values = set()

    # Convert each number to its distance from zero.
    for number in A:
        absolute_values.add(abs(number))

    # Return the number of distinct distances.
    return len(absolute_values)
