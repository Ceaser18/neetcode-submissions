class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxa=arr[0]
        current=arr[0]
        for i in range(1,len(arr)):
            current=max(arr[i],arr[i]+current)
            maxa=max(maxa,current)
        return maxa
        