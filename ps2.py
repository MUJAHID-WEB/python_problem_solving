#Problem 02:

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution: 

# To solve this problem in Python, we can use a hash map to store the values and their indices as we iterate through the array. For each number num in the array, we check if the complement of num (i.e., target - num) exists in the hash map. If it does, we found a pair that sums up to the target.

def twoSum(nums, target):
    # Create a hash map to store values and indices
    num_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        # Check if complement exists in the hash map
        if complement in num_map:
            # Return the indices of the two numbers
            return [num_map[complement], i]
        # Store the current number and its index in the hash map
        num_map[num] = i

    # No two numbers sum up to the target
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)

# Explanation:
# In the first example, the target is 9. The pair of numbers that sums up to 9 is (2, 7), and their indices in the array are (0, 1), respectively. Hence, the output is [0, 1].

# The code starts by initializing an empty hash map called num_map. Then, it iterates through the array using the enumerate() function, which provides both the index and the value of each element in the array.

# For each number num, the code calculates the complement by subtracting num from the target. It checks if the complement exists in the hash map using the in operator. If the complement is found, it means that we have already encountered a number that, when added to the current num, gives the target sum. In this case, the code returns the indices of the two numbers.

# If the complement is not found in the hash map, the code proceeds to store the current number num and its index i in the hash map.

# If no two numbers sum up to the target, the code returns an empty list [].

# This solution has a time complexity of O(n) since we iterate through the array once, and the hash map provides constant-time lookups.

