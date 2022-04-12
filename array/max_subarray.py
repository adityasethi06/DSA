# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the 
# largest sum and return its sum.

# A subarray is a contiguous part of an array.

# ----------------------------------------------------
# O(n^2) solution below

def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    max = 0
    for i, el1 in enumerate(nums):
        csum = el1
        for j, el2 in enumerate(nums):
            if j>i:
                csum += el2
                if csum > max:
                    max = csum

    return max


# print(maxSubArray([5,4,-1,7,8]))
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# ------------------------------------------------------

def maxSubArray2(nums):
    maxs = nums[0]
    curr = nums[0]
    for el in nums[1:]:
        curr = max(el+curr, el)
        maxs = max(curr, maxs)
    return maxs

# print(maxSubArray2([5,4,-1,7,8]))
print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))