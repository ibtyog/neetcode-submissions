class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr) - 1
        i = arr_len - 1
        start_val = 0
        max_val = arr[arr_len]
        while i >= 0:
            start_val = arr[i]
            arr[i] = max_val
            if start_val > max_val:
                max_val = start_val
            i-=1
        arr[arr_len] = -1
        return arr



        