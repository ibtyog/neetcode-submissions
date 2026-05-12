class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1,len(height)-1):
            left_max = max(height[0:i])
            right_max = max(height[i+1:])
            min_lr = min([left_max,right_max])
            res = min_lr - height[i]
            if res > 0:
                ans += res
        return ans