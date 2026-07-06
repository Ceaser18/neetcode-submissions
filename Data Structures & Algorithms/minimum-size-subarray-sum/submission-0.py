class Solution:
    def minSubArrayLen(self, k: int, arr: List[int]) -> int:
        left=0
        till_sum=0
        min_len = float('inf')
        for right in range(len(arr)):
            till_sum+=arr[right]
            while till_sum>=k:
                min_len = min(min_len,right-left+1)
                till_sum-=arr[left]
                left+=1
        return min_len if min_len!=float('inf') else 0

        