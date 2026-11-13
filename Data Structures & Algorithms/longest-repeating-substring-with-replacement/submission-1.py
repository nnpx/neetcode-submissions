class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find window with max length
        # constraint: k + maxF <= window

        l = 0
        count_hash_map = {}
        max_iden_str = 0
        maxf = 0
        for r in range(len(s)):
            # update hash_map: count of s[r] += 1
            if s[r] in count_hash_map: 
                count_hash_map[s[r]] += 1
            else:
                count_hash_map[s[r]] = 1
            
            # update maxf
            maxf = max(maxf, count_hash_map[s[r]])

            # shrink window by l+=1 when invalidate the constrint
            while k + maxf < (r - l + 1):
                count_hash_map[s[l]] -= 1
                l += 1

            max_iden_str = max(max_iden_str, r - l + 1) # length of window

        return max_iden_str
