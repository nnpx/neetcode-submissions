class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_n = set()
        for n in nums:
            if n in seen_n:
                return True
            else:
                seen_n.add(n)

        return False
        