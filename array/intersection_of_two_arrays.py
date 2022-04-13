# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.


# Below sol is O(n)
# ------------------------------------------------
def intersect(nums1, nums2):
        d = dict()
        for el in nums1:
            if el not in d:
                d[el] = [1, 0]
            else:
                d[el][0] += 1
        for el in nums2:
            if el not in d:
                d[el] = [0, 1]
            else:
                d[el][1] += 1
        
        return sum([ [k] * min(v[0], v[1]) for k, v in d.items() if (v[0] != 0 and v[1] != 0) ], [])

print(intersect([1,2,2,1], [2,2]))
# --------------------------------------------------