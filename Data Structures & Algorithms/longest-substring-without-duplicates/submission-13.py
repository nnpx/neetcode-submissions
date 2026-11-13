class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0
        last_seen = {}
        l, r = 0, 0
        while l < len(s) and r < len(s):
            if s[r] not in last_seen:
                last_seen[s[r]] = r
            else:
                l = max(last_seen[s[r]] + 1, l)
                last_seen[s[r]] = r
                
            longest_substr = max(longest_substr, r-l+1)
            r += 1

            # print("last_seen", last_seen)
            # print("substr_set", substr_set)
            # print(l,r)

        return longest_substr
        