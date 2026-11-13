# Problem 1: Distinct
# Return how many different numbers appear in A.

def solution(A):
    # Sets automatically remove duplicate values.
    unique_numbers = set()

    # Add every number to the set.
    for number in A:
        unique_numbers.add(number)

    # Count how many unique values remain.
    return len(unique_numbers)
