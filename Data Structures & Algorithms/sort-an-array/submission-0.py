class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr: List, start, end):
            if start >= end:
                return
            mid = (start + end) // 2
            mergeSort(arr, start, mid)
            mergeSort(arr, mid+1, end)
            merge(arr, start, mid, end)
        
        def merge(arr, start, mid, end):
            # calc left and right lengths
            leftLen = mid - start + 1
            rightLen = end - mid
            
            # empty arrays to include our merged result
            arrLeft = [0] * leftLen
            arrRight = [0] * rightLen

            #fill the empty arrays with results
            for i in range(leftLen):
                arrLeft[i] = arr[ i + start ]

            for j in range(rightLen):
                arrRight[j] = arr[ mid + j + 1 ]

            i = j = 0
            k = start

            # while i < leftLen and j < rightLen
            while i < leftLen and j < rightLen:
                if arrLeft[i] <= arrRight[j]:
                    arr[k] = arrLeft[i]
                    i += 1

                else:
                    arr[k] = arrRight[j]
                    j += 1
                k += 1

            while i < leftLen:
                arr[k] = arrLeft[i]
                i += 1
                k += 1
            while j < rightLen:
                arr[k] = arrRight[j]
                j += 1
                k += 1
        mergeSort(nums, 0, len(nums)-1)
        return nums