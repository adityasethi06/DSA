from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for ind, el in enumerate(nums):
            if (target - el) in d:
                return [d[target - el], ind]
            d[el] = ind