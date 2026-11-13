class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # central hash_map: {(0,0,1,0,0,2, ...): [words]}
        # for word in strs):
            # convert into [0,0,1,..]
            # convert to tuple
            # check if exist in hash map. if no, initiate. if yes, add words into [words]

        # loop hash map:
            # add each [words] into the return list
        # return list

        central_hash_map = {}
        for word in strs:
            char_count = [0]*26
            for char in word:
                char_count[ord(char)-ord('a')] += 1
            tuple_char_count = tuple(char_count)

            if tuple_char_count not in central_hash_map:
                central_hash_map[tuple_char_count] = [word]
            else:
                central_hash_map[tuple_char_count].append(word)

        return list(central_hash_map.values())
        # output_list = []
        # for words in central_hash_map.values():
        #     output_list.append(words)

        # return output_list
