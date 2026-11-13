class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window <= num of most frequent char + k
        
        count_char = {}
        max_substr = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            count_char[s[r]] = count_char.get(s[r], 0) + 1
            maxf = max(maxf, count_char.get(s[r]))

            # if window length in the constraint -> upd max_substr
            if r-l+1 <= maxf + k:
                max_substr = max(max_substr, r-l+1)
            # if not -> move l by 1, reduce count of s[l] by 1, 
            else:
                count_char[s[l]] -= 1
                l += 1

            # print(f"l {l}, r {r}, maxf {maxf}, max_substr {max_substr}")
           
        return max_substr