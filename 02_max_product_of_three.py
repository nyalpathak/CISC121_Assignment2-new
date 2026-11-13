# Problem 2: MaxProductOfThree
# Return the greatest product of any three distinct positions in A.

def solution(A):
    # Put the numbers in ascending order.
    numbers = sorted(A)

    # Candidate 1: multiply the three largest numbers.
    product_one = numbers[-1] * numbers[-2] * numbers[-3]

    # Candidate 2: two negative numbers can make a large positive product.
    product_two = numbers[0] * numbers[1] * numbers[-1]

    # Choose the larger product.
    return max(product_one, product_two)
