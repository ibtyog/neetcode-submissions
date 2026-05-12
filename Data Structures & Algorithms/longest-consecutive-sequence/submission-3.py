class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 1:
            return 0
        max = 1
        current = 1
        for num in range(1,len(nums)):
            if nums[num] == nums[num-1]+1:
                current += 1
            elif nums[num] == nums[num-1]:
                continue
            else:
                if current > max:
                    max = current
                current = 1
        if current > max:
            max = current
        return max

