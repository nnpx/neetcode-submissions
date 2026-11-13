class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # temp hash map: {num: freq}
        # [0,0,0,0] len is len(nums) + 1. Val=num. Index=how frequent that num occur

        # loop through nums
            # if num in temp_hash_map -> freq + 1
            # if not -> set freq = 1

        # transfrom temp_hash_map to array.
        # for num, freq in temp_hash_map.items()
            # arr[freq].append(num)
        
        # loop arr from the last index. return k numbers

        temp_hash_map = {}

        for num in nums:
            if num in temp_hash_map:
                temp_hash_map[num] += 1
            else:
                temp_hash_map[num] = 1
        # print(temp_hash_map)

        # temp_arr = [[]] * (len(nums) + 1) copies the reference to the same list in memory n times rather than creating new lists.
        temp_arr = [[] for _ in range(len(nums) + 1)]
        for num, freq in temp_hash_map.items():
            temp_arr[freq].append(num)
        # print(temp_arr)

        output_arr = []
        for num_arr in reversed(temp_arr):
            if k == 0:
                return output_arr
            for n in num_arr:
                output_arr.append(n)
                k -= 1

        return output_arr
        