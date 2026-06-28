class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        j=1
        for i in range(1,len(arr)):
            if arr[i]!=arr[j-1]:
                arr[j]=arr[i]
                j+=1
        return j
        