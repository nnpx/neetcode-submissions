class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map: {target-n: location}

        # loop the array
            # if n in the hash_map -> return hash_map[target-n], loaction of n

        target_dict = {}
        for i in range(len(nums)):
            if nums[i] in target_dict:
                return [target_dict[nums[i]], i]
            else:
                target_dict[target - nums[i]] = i
        