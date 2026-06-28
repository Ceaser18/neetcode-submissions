class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l=0
        r=len(arr)-1
        while l<r:
            current=arr[l]+arr[r]
            if current==target:
                return [l+1,r+1]
            elif current<target:
                l+=1
            else:
                r-=1
        return []

        