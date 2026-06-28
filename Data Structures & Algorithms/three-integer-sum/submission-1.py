class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        ans=[]
        nums = sorted(arr)
        for i,num in enumerate(nums):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue
            while l<r:
                current = nums[l]+nums[r]+num
                if current==0:
                    ans.append([nums[l],nums[r],num])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and nums[r+1]==nums[r]:
                        r-=1
                elif current<0:
                    l+=1
                else:
                    r-=1
        return ans