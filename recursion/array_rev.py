
# recursive
def rev_arr(arr):
    if len(arr) == 1:
        return arr
    return arr[-1:] + rev_arr(arr[:-1])

# print(rev_arr([1,2,3,4,5]))

# two pointer recursive
def rev_arr2(l, r, a):
    if l>r:
        return
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1
    rev_arr2(l,r,a)

# arr = [1,2,3]
# rev_arr2(0, len(arr)-1, arr)
# print(arr)


s = []
def isPalindrome(i, str):
    if i >= len(str)/2:
        return True
    ch_matches = str[i] == str[len(str)-1-i]
    i += 1
    s.append(ch_matches)
    return ch_matches and isPalindrome(i,str) if ch_matches else False

print(isPalindrome(0, "anggggna"))
print(s)
