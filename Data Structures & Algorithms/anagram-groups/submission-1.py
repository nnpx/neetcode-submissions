class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # central_hash_map: {letter_count_tuple: [word1, word2], ...}

        # loop through the strs
            # transform into letter_count_tuple
                # letter_count_list = [0] * 26
                # loop through each letter; 
                    # +1 in its ord - ord("a")

            # if the letter_count_tuple is in the central_hash_map -> add the word
            # if not -> add the letter_count_tuple into the central_hash_map

        # return the [each value in the central_hash_map]

        central_hash_map = {}

        # transform word into letter_count_list -> letter_count_tuple
        for word in strs:
            letter_count_list = [0] * 26
            for l in word:
                letter_count_list[ord(l) - ord("a")] += 1
            letter_count_tuple = tuple(letter_count_list)

            # add {letter_count_tuple: [word]} into the central_hash_map
            if letter_count_tuple in central_hash_map:
                central_hash_map[letter_count_tuple].append(word)
            else:
                central_hash_map[letter_count_tuple] = [word]

        return list(central_hash_map.values())