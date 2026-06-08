class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # store occurences, we know that we have only 3 distinct values
        # only 3 values: 0, 1, 2
        count = [0] * 3
        # use values as indices, for each value in nums -> incrememnt occurence by 1
        for num in nums:
            count[num] += 1

        # declare var to be the index on the nums array
        index = 0
        # for each distinct num in nums
        for distinctNum in range(3):
            # while count[distinct num] is not zero "already occurs"
            while count[distinctNum]:
                # decrement the value in count by 1
                count[distinctNum] -= 1
                # replace the current value in nums by the distinct num
                nums[index] = distinctNum
                # increase index by 1
                index += 1

