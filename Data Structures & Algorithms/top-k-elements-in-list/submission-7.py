class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # convert to count hash map
        count = {}
        for n in nums:
            if n in count: 
                count[n] += 1
            else:
                count[n] = 1

        # convert to [x,x,x,x,x] each x rep the number x appear i times; len = len(nums)
        freq = [[] for i in range(len(nums)+1)]
        for n in count:
            freq[count[n]].append(n)

        # loop from the back k times
        ret = []
        for i in range(len(freq)-1, 0, -1):
            if freq[i] != [] and k > 0:
                ret += freq[i]
                k -= len(freq[i])
        return ret
        