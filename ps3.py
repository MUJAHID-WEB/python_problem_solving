#Problem 03:
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 
# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

# Solution:

def totalFruit(fruits):
    max_fruits = 0
    fruit_counts = {}
    start = 0

    for end in range(len(fruits)):
        # Add the current fruit to the fruit_counts dictionary
        fruit_counts[fruits[end]] = fruit_counts.get(fruits[end], 0) + 1

        # Shrink the window until we have at most 2 different types of fruits
        while len(fruit_counts) > 2:
            fruit_counts[fruits[start]] -= 1
            if fruit_counts[fruits[start]] == 0:
                del fruit_counts[fruits[start]]
            start += 1

        # Update the maximum number of fruits
        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits

# Example usage
fruits = [1, 2, 1]
result = totalFruit(fruits)
print(result)



# Explanation:

# In the first example, the given list of fruits is [1, 2, 1]. We can pick fruits from all three trees because they are the same type or fit into our two baskets. Therefore, the maximum number of fruits we can pick is 3.

# The code iterates through the list of fruits using the end pointer. It keeps track of the count of each fruit type in the fruit_counts dictionary. The start pointer is used to shrink the window until we have at most 2 different types of fruits in the window. Whenever we encounter a third fruit type, we adjust the start pointer to exclude the earliest fruit and update the fruit_counts accordingly.

# By keeping track of the maximum number of fruits seen so far, we can return the final maximum number of fruits we can pick.

# This sliding window approach has a time complexity of O(n), where n is the length of the input array fruits. We iterate through the array once, and at each iteration, we perform constant-time operations to update the fruit_counts dictionary and calculate the maximum number of fruits.