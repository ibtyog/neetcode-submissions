class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        k_nums = []
        for num in nums:
            if num in dict:
                dict[num] += 1
                continue
            dict[num] = 1
        for i in range(k):
            max_val = max(dict, key=dict.get)
            k_nums.append(max_val)
            del dict[max_val]
        return k_nums
