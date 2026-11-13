class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output_list = []
        nums.sort()
        for i in range(len(nums)-1):
            # all remaining numbers are positive
            if nums[i] > 0: 
                break 
            # Skip duplicate values
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            # find 2 sums with 2 pointers bc array is sorted
            target_sum = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                current_sum = nums[l] + nums[r]
                if current_sum < target_sum:
                    l += 1
                elif current_sum > target_sum:
                    r -= 1
                else:
                    output_list.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # Skip duplicate values
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                        
        return output_list

        