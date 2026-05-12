class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        l = 0
        r = len(heights) - 1
        while r > l:
            v = (r-l) * min([heights[l], heights[r]])
            if v > max_v:
                max_v = v
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        return max_v
