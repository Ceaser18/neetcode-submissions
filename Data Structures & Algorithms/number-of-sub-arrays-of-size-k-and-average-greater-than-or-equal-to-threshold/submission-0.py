class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        left=0
        moving_sum=0
        for right in range(len(arr)):
            moving_sum+=arr[right]
            if right-left+1>k:
                moving_sum-=arr[left]
                left+=1
            if right-left+1 == k:
                if moving_sum>=k*threshold:
                    count+=1
        return count