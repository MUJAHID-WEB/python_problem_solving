# Problem 11: ( Build Array from Permutation )

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 
# Example 1:

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]

# Example 2:

# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.
 

# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?




# Solution: 

# To solve this problem in Python, we can iterate through the given array nums and build the resulting array ans using the given formula ans[i] = nums[nums[i]].

# Here's the Python code to solve the problem:

def build_array(nums):
    n = len(nums)
    ans = [0] * n

    for i in range(n):
        ans[i] = nums[nums[i]]

    return ans

# Explanation:

# We initialize an empty array ans with the same length as nums to store the resulting array.
# We iterate through each index i in the range from 0 to n-1, where n is the length of nums.
# For each index i, we set ans[i] to nums[nums[i]] using the given formula.
# Finally, we return the resulting array ans.
# The chosen algorithm works because it effectively applies the given formula to each index of the array nums and stores the result in the corresponding index of the resulting array ans. By iterating through each index once, we can build the entire ans array.

# The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we need to iterate through each index once to build the resulting array ans. The space complexity is also O(n) since we need to create an array of the same length as nums to store the result.

# The algorithm does not require any extra space apart from the resulting array ans, making it an efficient solution in terms of memory usage.