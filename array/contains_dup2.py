# Given an integer array nums and an integer k, return true if there are two distinct indices 
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


def containsNearbyDuplicate(nums, k):
        d = dict()
        for ind , el in enumerate(nums):
            if el not in d:
                d[el] = ind
            if el in d:
                if ind != d[el] and abs(ind-d[el]) <= k:
                    return True
                d[el] = ind
        return False