class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1