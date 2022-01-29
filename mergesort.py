

def mergesort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged_lst = []
    i, j = 0, 0

    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            merged_lst.append(left[i])
            i += 1
        else:
            merged_lst.append(right[j])
            j += 1

    if j<len(right):
        while j<len(right):
            merged_lst.append(right[j])
            j += 1

    if i<len(left):
        while i<len(left):
            merged_lst.append(left[i])
            i += 1

    return merged_lst


print(mergesort([17,21,29,38,1,14]))