class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[j] > heights[i]:
                    max_heights = heights[i]
                else:
                    max_heights = heights[j]
                if max_heights * (j - i) > max_v:
                    max_v = max_heights * (j - i)
        return max_v