class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_substr = 0
        l = 0
        for r in range(len(s)):
            if s[r] in char_index:
                l = max(l, char_index.get(s[r]) + 1)
            
            char_index[s[r]] = r
            max_substr = max(max_substr, r-l+1)

            # print(max_substr)
            # print(l, r, s[l:r+1])

        return max_substr
            
        