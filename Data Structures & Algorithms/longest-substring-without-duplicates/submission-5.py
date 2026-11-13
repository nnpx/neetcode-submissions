class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hash_map = {}
        max_substr = 0
        
        for r in range(len(s)):
            if s[r] not in hash_map:
                hash_map[s[r]] = r
            else:
                l = max(hash_map[s[r]] + 1, l)
                hash_map[s[r]] = r
            max_substr = max(max_substr, r - l + 1)
        return max_substr
                
        