import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storeCount = {}
        for number in nums:
            if number in storeCount:
                storeCount[number] += 1
            else:
                storeCount[number] = 1
        return heapq.nlargest(k, storeCount.keys(), key=storeCount.get)