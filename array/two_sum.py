# return index of 2 nos that add up to a given target
# below algo use extra space O(N). works on unordered list of nums
class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for ind, el in enumerate(nums):
            if (target - el) in d:
                return [d[target - el], ind]
            d[el] = ind

# what is list is ordered? can we solve without extra space?
# eg: [1,3,5,7,11,13], target = 12
# assume that there exists a pair that will add up to target

def twoSum(nums, target):
    l,r = 0, len(nums)-1
    while l<r:
        current_sum = nums[l] + nums[r]
        if current_sum > target: 
            r -= 1  # need to reduce sum, so need to shift r pointer to left.
        elif current_sum < target:
            l += 1  # need to reduce sum, so need to shift l pointer to right.
        else:
            return [l,r]

print(twoSum([1,3,5,7,14,15], 12))
    
