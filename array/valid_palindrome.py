# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward 
# and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s):
        alnum = [c.lower() for c in s if c.isalnum()]
        if not alnum:
            return True
        
        i = 0
        j = len(alnum)-1
        
        while i<j:
            if alnum[i] != alnum[j]:
                return False
            i += 1
            j -= 1
        return True

print(isPalindrome("A man, a plan, a canal: Panama"))