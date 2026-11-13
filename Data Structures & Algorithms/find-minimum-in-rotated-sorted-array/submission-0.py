class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0] # cannot set as 0 because num can be (-)
        l, r = 0, len(nums)-1
        
        while l <= r:
            # If nums[l:r+1] is sorted -> min is value at l
            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l])
                break
            
            # compare every value at m as the minimum
            m = (l + r) // 2
            min_num = min(min_num, nums[m])
            
            # key idea: (ex. [2 3 4] [5 0 1]) one part is always sorted, 
            # and the other part contains the rotation (and the minimum element)
            if nums[l] <= nums[m]:  # left is sorted
                l = m + 1           # -> go right + skip m (bc already consider m as min)
            else:                   # left is not sorted
                r = m - 1           # -> go left + skip m (bc already consider m as min)

        return min_num