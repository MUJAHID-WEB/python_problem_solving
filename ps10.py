# Problrm 10:

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 



# Solution:

# To increment a large integer represented as an array of digits by one, we can follow these steps:

# Initialize a carry variable to 1. This represents the value that needs to be added to the least significant digit.

# Iterate through the digits in reverse order (from right to left):

# Add the carry to the current digit.
# Update the carry by dividing the sum by 10 (carry = sum // 10).
# Update the current digit by taking the modulo 10 of the sum (digit = sum % 10).
# If the carry becomes zero, exit the loop since there is no need to continue incrementing.
# If the carry is still non-zero after the loop, it means we need to add an additional digit to the leftmost side. Append the carry to the left of the digits array.

# Return the updated digits array.

def plusOne(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        sum = digits[i] + carry
        digits[i] = sum % 10
        carry = sum // 10
        if carry == 0:
            break

    if carry != 0:
        digits.insert(0, carry)

    return digits

# Let's test the function with the provided examples:

print(plusOne([1, 2, 3]))   # Output: [1, 2, 4]
print(plusOne([4, 3, 2, 1])) # Output: [4, 3, 2, 2]
print(plusOne([9]))          # Output: [1, 0]

# The function correctly increments the large integer by one and returns the resulting array of digits.