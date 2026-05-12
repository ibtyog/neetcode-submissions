class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        current = 0
        for i in nums:
            if i == 1:
                current+=1
            else:
                if current > max_con:
                    max_con = current
                current = 0
        if current > max_con:
            return current
        return max_con