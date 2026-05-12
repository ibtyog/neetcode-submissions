class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        for num in range(len(nums)):
            for scd_num in range(len(nums)):
                for trd_num in range(len(nums)):
                    if num == scd_num or scd_num == trd_num or num == trd_num:
                        continue
                    else:
                        temp = [nums[num],nums[scd_num],nums[trd_num]]
                    if sum(temp) == 0:
                        temp.sort()
                        if temp not in solution:
                            solution.append(temp)
        return solution