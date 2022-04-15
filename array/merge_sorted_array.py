# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored 
# inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first 
# m elements denote the elements that should be merged, and the last n elements are set to 0 
# and should be ignored. nums2 has a length of n.

# Constraints:

#     nums1.length == m + n
#     nums2.length == n

# Example 1:

#     Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#     Output: [1,2,2,3,5,6]
#     Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#     The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

#     Input: nums1 = [1], m = 1, nums2 = [], n = 0
#     Output: [1]
#     Explanation: The arrays we are merging are [1] and [].
#     The result of the merge is [1].

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        curr = m+n-1
        
        while j>=0 and i>=0 and curr>=0:  # we need to transfer all el from nums2 to nums1. j == -1 means all transfered
            if nums2[j] >= nums1[i]:
                nums1[curr] = nums2[j]
                j -= 1
            else:
                nums1[curr] = nums1[i]
                i -= 1
            curr -= 1
        if j>=0: # means that all elements from nums 2 have not been transfered to nums1 and nums1 got exhausted. now we just need to copy stuff.
            while j>=0 and curr>=0:
                nums1[curr] = nums2[j]
                j -= 1
                curr -= 1
        return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))