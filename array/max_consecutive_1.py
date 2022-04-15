# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Success > Details 
# Runtime: 331 ms, faster than 99.85% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.2 MB, less than 82.52% of Python3 online submissions for Max Consecutive Ones.

def findMaxConsecutiveOnes(nums):
        maxn = 0
        curr_streak = 0
        for el in nums:
            if el:
                curr_streak += 1
                continue
            maxn = max(maxn, curr_streak)
            curr_streak = 0
        return max(maxn, curr_streak)