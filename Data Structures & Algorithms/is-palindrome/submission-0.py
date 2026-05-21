class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(cleanS) - 1
        while i < j:
            if cleanS[i] != cleanS[j]:
                return False
            i += 1
            j -= 1
        return True