class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        left = [0]*n
        right=[0]*n
        for i in range(1,n):
            left[i] = max(left[i-1],arr[i-1])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],arr[i+1])
        water=0
        for i in range(n):
            amount=min(left[i],right[i])-arr[i]
            if amount>0:
                water+=amount
        return water
