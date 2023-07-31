# Problem 05:

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Solution:

# To solve this problem in Python with a time complexity of O(n), we can use a hash set to store all the numbers in the array. Then, for each number num in the array, we check if num-1 exists in the hash set. If it does not, it means num is the start of a consecutive sequence. We can then iterate from num onwards, incrementing a counter until we encounter a number that does not exist in the hash set. We keep track of the maximum length of consecutive elements sequence found so far.

def longestConsecutive(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# # Example usage
nums = [100, 4, 200, 1, 3, 2]
result = longestConsecutive(nums)
print(result)

# Output:
# 4

# Explanation:

# In the first example, the input array is [100, 4, 200, 1, 3, 2]. The longest consecutive elements sequence in the array is [1, 2, 3, 4], which has a length of 4. Therefore, the output is 4.

# The code starts by creating a hash set called num_set and storing all the numbers from the input array in it. This allows us to perform constant-time lookups to check if a number exists in the set.

# Next, it initializes a variable called max_length to keep track of the maximum length of consecutive elements sequence found so far.

# Then, it iterates through the numbers in the set. For each number num, it checks if num - 1 exists in the set. If it does not, it means that num is the start of a consecutive sequence.

# Inside the while loop, we have current_num initialized to num and current_length initialized to 1. We increment current_num and current_length as long as current_num + 1 exists in the set. This allows us to iterate through the consecutive elements sequence starting from num and count its length.

# After the while loop, we update max_length with the maximum value between max_length and current_length. This ensures that we keep track of the longest consecutive elements sequence found so far.

# Finally, we return max_length, which represents the length of the longest consecutive elements sequence in the array.

# This solution has a time complexity of O(n) because we iterate through the numbers in the input array once and perform constant-time operations for each number. The hash set provides efficient lookup and insertion operations, resulting in an overall linear time complexity.