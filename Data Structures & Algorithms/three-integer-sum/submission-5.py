class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # output []
        # nums.sort()
        # for i in range(len(nums)):
            # if same value with the before index -> continue
            # calculate the target: 0 - current_num
            # find 2 sums
            # set()
            # for j in range(i, len(nums)):
                # find 3rd_n = target-nums[j]
                # if 3rd_n not in set -> add, if 3rd_n in set output.append

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
                    print(i,l,r)
                    output_list.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # Skip duplicate values
                    while l < r and nums[l-1] == nums[l]:
                        l += 1

        return output_list

        