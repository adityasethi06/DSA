
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false



def isAnagram(s, t):
        d = dict()
        d1 = dict()
        for c in t:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for c in s:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1
        return d == d1