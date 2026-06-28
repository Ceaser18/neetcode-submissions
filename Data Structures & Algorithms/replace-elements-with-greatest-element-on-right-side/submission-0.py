class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_r=-1
        for i in range(len(arr)-1,-1,-1):
            new_max = max(max_r,arr[i])
            arr[i]=max_r
            max_r = new_max 
        return arr
        