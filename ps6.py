#Problem 06:

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# To solve this problem in Python with a time complexity of O(log n), we can use the binary search algorithm. Since the input array is already sorted, we can search for the target value by repeatedly dividing the search space in half.

# Here's the Python code to solve the problem:

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# # Example usage
nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(result)

# Output:
# 2


# Explanation:
# In the first example, the input array is [1, 3, 5, 6], and the target value is 5. We need to find the index where the target value is found or the index where it would be inserted if it were not found.

# The code initializes two pointers, left and right, pointing to the start and end of the array, respectively. It enters a while loop where it calculates the middle index as (left + right) // 2. It then compares the value at the middle index with the target value.

# If the value at the middle index is equal to the target value, it means we have found the target value, and we return the middle index.

# If the value at the middle index is less than the target value, we adjust the left pointer to mid + 1 to search the right half of the array.

# If the value at the middle index is greater than the target value, we adjust the right pointer to mid - 1 to search the left half of the array.

# We continue this process, repeatedly dividing the search space in half until the left pointer surpasses the right pointer, indicating that we have found the position where the target value should be inserted.

# Finally, we return the left pointer as the index where the target value should be inserted.

# This solution has a time complexity of O(log n) because the binary search algorithm reduces the search space by half in each iteration. The logarithmic time complexity is achieved by dividing the search space in half repeatedly until the target value is found or the search space is empty.