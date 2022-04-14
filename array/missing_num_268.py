# Given an array nums containing n distinct numbers 
# in the range [0, n], return the only number in the range that is missing from the array.

# solved in 0(n) and with less mem consumption using generator

def missingNumber(nums):
        expected_sum = 0
        for no in (n for n in range(0, len(nums)+1)):
            expected_sum += no
        return expected_sum - sum(nums)

print(missingNumber([3,0,1]))