class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # calculate maj = len(nums) // 2
        #create dict to store appearance
        # loop on dict items, if value > maj, return the key
        if len(nums) == 1:
            return nums[0]
        maj = len(nums) // 2
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num] += 1
                if countDict[num] > maj:
                    return num
            else:
                countDict[num] = 1
