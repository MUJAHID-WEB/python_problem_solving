# Problem 04:

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Solution:

# To solve this problem in Python, we can use the Two-Pointers technique. We'll have two pointers, left and right, initially pointing to the start and end of the array, respectively. We'll move the right pointer from right to left, and whenever we encounter the value val, we'll replace it with the value at the left pointer (if it's not val). We'll then move both pointers inward until they meet. Finally, we'll return the position of the left pointer as the number of elements not equal to val.

def removeElement(nums, val):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[right] == val:
            right -= 1
        elif nums[left] == val:
            nums[left] = nums[right]
            left += 1
            right -= 1
        else:
            left += 1

    return left

# # Example usage
nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print(result)
print(nums[:result])  # Printing the elements not equal to val

# Output:
# 2
# [2, 2]

# Explanation:

# In the first example, the given list of numbers is [3, 2, 2, 3] and the value to remove is 3. We need to remove all occurrences of 3 from the list and return the number of elements not equal to 3. After removing 3, the list becomes [2, 2, _, _], where _ represents any value. The elements not equal to 3 are 2 and 2, so the output is 2.

# The code initializes two pointers, left and right, pointing to the start and end of the array, respectively. It enters a while loop where it compares the values at the left and right pointers with the value val.

# If the value at the right pointer is val, it means it should be removed, so we decrement the right pointer.

# If the value at the left pointer is val, we replace it with the value at the right pointer (if it's not val), increment the left pointer, and decrement the right pointer.

# If the value at the left pointer is not val, we increment the left pointer.

# We continue this process until the left pointer surpasses the right pointer, indicating that we have processed all the elements in the array.

# Finally, we return the position of the left pointer as the number of elements not equal to val. We also print the elements not equal to val using array slicing (nums[:result]).

# This solution has a time complexity of O(n), where n is the length of the input array nums. We traverse the array once using the two pointers, performing constant-time operations at each step.