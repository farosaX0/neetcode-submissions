class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupDict = {}
        for n in nums:
            if n in dupDict:
                dupDict[n] += 1
                if dupDict[n] > 1:
                    return True
                
            else:
                dupDict[n] = 1
        return False