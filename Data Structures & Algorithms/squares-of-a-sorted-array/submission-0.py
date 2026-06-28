class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        l,r=0,n-1
        for i in range(n-1,-1,-1):
            if abs(arr[l])>abs(arr[r]):
                res[i] = arr[l]**2
                l+=1
            else:
                res[i] = arr[r]**2
                r-=1
        return res
        