# Problem 5: MinAbsSumOfTwo
# Find the smallest absolute sum of two elements of A.
# Codility permits choosing the same array position twice.

def solution(A):
    # Sort the numbers to make it easy to move toward zero.
    numbers = sorted(A)

    # Begin with the smallest and largest numbers.
    left = 0
    right = len(numbers) - 1
    smallest_sum = abs(numbers[left] + numbers[right])

    # The two positions may be the same.
    while left <= right:
        # Find the sum and its absolute value.
        pair_sum = numbers[left] + numbers[right]
        absolute_sum = abs(pair_sum)

        # Remember the smallest value seen so far.
        if absolute_sum < smallest_sum:
            smallest_sum = absolute_sum

        # No absolute value can be less than zero.
        if smallest_sum == 0:
            return 0

        # Adjust the sum toward zero.
        if pair_sum < 0:
            left += 1
        else:
            right -= 1

    return smallest_sum
