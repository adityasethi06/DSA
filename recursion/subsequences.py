# write a func to print all subsequences
# A subsequence is a contigous/non-contigous squence but follows orig order
# also print how many subsequences match with a given target

def subseq(ind, arr, matches, target, output=None):
    if not output:
        output = ['']*len(arr)
    if ind >= len(arr):
        ss = ''.join([str(o) for o in output])
        print(ss)
        if ss == target:
            matches.append(ss)
        return
    output[ind] = arr[ind]
    ind += 1
    subseq(ind, arr, matches, target, output)
    ind -= 1
    output[ind] = ''
    ind += 1
    subseq(ind, arr, matches, target, output)

matches = []
subseq(0, [1,2,2,3], matches, '223')
print(matches)
