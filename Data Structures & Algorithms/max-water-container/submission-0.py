class Solution:
    def maxArea(self, arr: List[int]) -> int:
        max_water = 0
        l,r=0,len(arr)-1 # we are using 2 pointers here 
        while l<r:
            width=r-l
            height = min(arr[l],arr[r])
            area = width*height
            max_water = max(max_water,area)
            if arr[l]<arr[r]:
                l+=1
            else:
                r-=1
        return max_water
        