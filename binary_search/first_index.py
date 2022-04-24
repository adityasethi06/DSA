# find 1st index of element in a sorted list if it exists else return -1

def first_index_of(el, arr):
    l = 0
    r = len(arr)-1
    ind = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == el:
            ind = mid
            r = mid-1
        elif arr[mid] > el:
            r = mid-1
        else:
            l = mid+1
    return ind

print(first_index_of(3, [1,2,2,3,3,5,6,7]))
