# get shortest word dist b/w two words
# the shortest dist b/w 'hi' and 'bye' is 1 in below array (index 5 anf 6)
# ['hi', 'alpha', 'charlie', 'bye', 'tom', 'adi', 'bye', 'hi']

def shortestDist(w1, w2, words):
    i = -1  # will stop at every 'hi' w1
    j = -1 # will stop at every 'bye' w2
    dist = -1
    for ind, w in enumerate(words):
        if w == w1:
            i = ind
        if w == w2:
            j = ind
        if words[i] == w1 and words[j] ==  w2:
            dist = abs(j-i) if dist < 0 else min(dist, abs(j-i))
    return dist
    

a = ['hi', 'alpha', 'charlie', 'pink', 'tom', 'adi', 'bye', 'h', 'hiii']
print(shortestDist('hi', 'bye', a))