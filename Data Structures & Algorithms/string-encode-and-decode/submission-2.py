from typing import List


class Solution:

    # ["Hello","World"] -> 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        encoded_strs_list = []
        for s in strs:
            encoded_strs_list.append(str(len(s)))
            encoded_strs_list.append('#')
            encoded_strs_list.append(s)
        return "".join(encoded_strs_list)

    # 5#Hello5#World -> ["Hello","World"]
    def decode(self, s: str) -> List[str]:
        decoded_strs_list = []
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            i = j
            while s[j] != '#':
                j += 1
            len_str = int(s[i:j])
            str = s[j+1: j+1+len_str]
            decoded_strs_list.append(str)
            j = j+1+len_str
        return decoded_strs_list

        