class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleanS = "".join(char.lower() for char in s if char.isalnum())
        def isPalindrome(l, r):
            while l < r:
                if cleanS[l] != cleanS[r]:
                    return False
                l += 1
                r -= 1
            return True
        i = 0
        j = len(cleanS) - 1
        while i < j:
            if cleanS[i] != cleanS[j]:
                return isPalindrome(i+1, j) or isPalindrome(i, j-1)
            i += 1
            j -= 1
        return True