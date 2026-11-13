class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            
            # left side [l...mid] is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1 # Target is inside the sorted left half -> go left
                else:
                    l = m + 1
            # right side [mid...r] is sorted
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1 # Target is inside the sorted right half -> go right
                else:
                    r = m - 1

        return -1