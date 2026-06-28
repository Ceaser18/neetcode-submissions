class Solution:
    def twoSum(self, arr: List[int], k: int) -> List[int]:
        l,r=0,len(arr)-1
        while l<r:
            s=arr[l]+arr[r]
            if s==k:
                return [l+1,r+1]
            elif s<k:
                l+=1
            else:
                r-=1
        return -1

        