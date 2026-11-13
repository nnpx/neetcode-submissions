class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1
        while l < r:
            # calculate area -> choose max
            current_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(current_area, max_area)
            print(max_area)

            # move the shorter pointer
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


        