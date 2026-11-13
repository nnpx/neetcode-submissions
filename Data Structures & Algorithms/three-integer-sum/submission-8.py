class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # loop through each num
        # skip if have same val with the one before + if i > 0
            # 2 sums using pointers
            # l, r = i+1, len(nums)-1
            # l += 1 if num[l+1] has the same value with before

        output_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                current_sum = nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                            l += 1

                elif current_sum > target:
                    r -= 1
                else:
                    output_list.append([nums[i], nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                            l += 1
        
        return output_list
                
