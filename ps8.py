# Problem 08:

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Solution

# To solve this problem in Python, you can use two pointers to track the current position while iterating through the array. Here's a step-by-step explanation of the approach:

# 1. Initialize two pointers, i and j, both starting at index 0.
# 2. Iterate through the array starting from index 1:
# 3. If the element at the current index is different from the element at index j, update the element at index j+1 with the current element, and increment j by 1.
# 4. After the iteration, the first j+1 elements in the array will contain the unique elements in their original order.
# 5. Return the value of j+1 as the number of unique elements.

# Here's the Python code that implements this approach:


def removeDuplicates(nums): # The function removeDuplicates takes an array nums as input.
    if not nums:
        return 0   # The first line checks if the array is empty. If it is, there are no elements to remove, so it returns 0. 
    
    j = 0 # Two pointers, i and j, are initialized to 0.

    for i in range(1, len(nums)): #The for loop iterates through the array starting from index 1 (since the first element doesn't need to be compared). 

        if nums[i] != nums[j]: # In each iteration, it checks if the element at the current index i is different from the element at index j. If they are different, it means a new unique element has been found.

            j += 1 # In that case, j is incremented by 1, and the element at index j is updated with the current element at index i. This effectively removes duplicates and keeps track of the unique elements in the first part of the array.

            nums[j] = nums[i]

    return j + 1  # Finally, the function returns j + 1, which represents the number of unique elements in the modified array.

# Let's test the function with the provided examples:


nums1 = [1, 1, 2]
expected1 = [1, 2]
k1 = removeDuplicates(nums1) # It calls the removeDuplicates function with the nums1 array and stores the returned value in k1.
print(k1)  # Then it prints k1, which represents the number of unique elements in nums1. # Output: 2 
print(nums1[:k1])  # Finally, it prints nums1[:k1], which represents the modified array containing only the unique elements. # Output: [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected2 = [0, 1, 2, 3, 4]
k2 = removeDuplicates(nums2)
print(k2)  # Output: 5
print(nums2[:k2])  # Output: [0, 1, 2, 3, 4]

# The function correctly removes the duplicates in-place while maintaining the order of the unique elements, and it returns the number of unique elements as expected.