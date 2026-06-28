class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n=len(arr)
        output = [1]*n
        for i in range(1,n):
            output[i] = output[i-1]*arr[i-1]
        right=1
        for i in range(n-1,-1,-1):
            output[i]*=right
            right*=arr[i]
        return output
        