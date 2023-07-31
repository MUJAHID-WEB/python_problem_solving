# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 


# Solution:

# To reverse the digits of a signed 32-bit integer, we can follow these steps:

# 1. Check if the input integer x is negative. If it is, store the sign and convert x to a positive number for the reversal process. This step ensures that the sign is preserved after the reversal.

# 2. Initialize a variable rev to 0, which will store the reversed number.

# 3. Iterate until x becomes 0:

#    a. Get the last digit of x by taking the modulo 10: last_digit = x % 10.
#    b. Update x by dividing it by 10 and discarding the last digit: x //= 10.
#       Multiply rev by 10 and add the last_digit to it: rev = rev * 10 + last_digit.
# 4. After the iteration, check if the reversed number rev exceeds the 32-bit signed integer range [-2^31, 2^31 - 1]. If it does, return 0.

# 5. If the original input x was negative, multiply the rev by -1 to restore the sign.

# 6. Return the reversed number rev.

# Here's the implementation of the above algorithm in Python:

def reverse(x):
    if x < 0:
        sign = -1
        x = abs(x)
    else:
        sign = 1

    rev = 0
    while x != 0:
        last_digit = x % 10
        x //= 10
        rev = rev * 10 + last_digit

    rev *= sign

    # Check if the reversed number is within the 32-bit signed integer range
    if rev < -2**31 or rev > 2**31 - 1:
        return 0

    return rev

# Let's test the function with the provided examples:


print(reverse(123))   # Output: 321
print(reverse(-123))  # Output: -321
print(reverse(120))   # Output: 21

# The function correctly reverses the digits of the input integers and handles the edge case of exceeding the signed 32-bit integer range.