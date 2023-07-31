# Problem 07:

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
# Solution

# To solve this problem in Python without using any built-in exponent function or operator, we can use the binary search algorithm to find the square root of the given non-negative integer x.

def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

# # Example usage
x = 8
result = mySqrt(x)
print(result)

# Output:
# 2

# Explanation:
# In the example, the input is x = 8, and we need to find the square root of x rounded down to the nearest integer.

# The code starts by handling the base case where x is 0, in which case the square root is also 0. We return 0 in this case.

# For non-zero values of x, the code initializes two pointers, left and right, representing the search space. left is initialized to 1, and right is initialized to x.

# The code enters a while loop where it calculates the middle index as (left + right) // 2. It then compares the square of the middle index with x.

# If the square of the middle index is equal to x, it means we have found the square root, and we return the middle index.

# If the square of the middle index is less than x, we adjust the left pointer to mid + 1 to search the right half of the search space.

# If the square of the middle index is greater than x, we adjust the right pointer to mid - 1 to search the left half of the search space.

# We continue this process, repeatedly dividing the search space in half until the left pointer surpasses the right pointer, indicating that we have found the position where the square root should be.

# Finally, we return the right pointer as the square root rounded down to the nearest integer.

# This solution has a time complexity of O(log x) because the binary search algorithm reduces the search space by half in each iteration. The logarithmic time complexity is achieved by dividing the search space in half repeatedly until the square root is found or the search space is empty.