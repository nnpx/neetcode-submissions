class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [[],[],[]] len is len(nums). index 0 represent lists of number that have frequency 1
        # nums_count_hash_map = {number: freq}

        # loop nums:
            # append to hash_map if not already in it. If not, initiate

        #  loop hash_map:
            # append number into the inner list in index frequency - 1

        # output_list = []
        # last_index
        # while len(output_list) < k:
            # append numbers in the output_list 
            # index -= 1

        nums_count_hash_map = {}
        for num in nums:
            if num not in nums_count_hash_map:
                nums_count_hash_map[num] = 1
            else:
                nums_count_hash_map[num] += 1
        
        # convert to list
        freq_list = [[] for i in range(len(nums))]
        for num, freq in nums_count_hash_map.items():
            freq_list[freq - 1].append(num)

        # output first k most frequent
        output_list = []
        for num_list in reversed(freq_list):
            if len(output_list) < k:
                output_list += num_list
        return output_list