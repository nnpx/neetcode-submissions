class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for l in s:
            if not s_count.get(l):
                s_count[l] = 1
            else:
                s_count[l] += 1
        print(s_count)

        for l in t:
            if not t_count.get(l):
                t_count[l] = 1
            else:
                t_count[l] += 1
        print(t_count)

        return s_count == t_count