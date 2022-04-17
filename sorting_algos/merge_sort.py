def merge(l1,l2):
    merged = []
    i,j = 0,0
    while i<len(l1) and j<len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    while i<len(l1):
        merged.append(l1[i])
        i += 1
    while j<len(l2):
        merged.append(l2[j])
        j += 1
    return merged


def mergeSort(l):
    if len(l) == 1:
        return l
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    r1 = mergeSort(left)
    r2 = mergeSort(right)
    return merge(r1, r2)

print(mergeSort([3,7,8,9,1,11,5]))