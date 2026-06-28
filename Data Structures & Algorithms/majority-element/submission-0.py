class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        return [num for num,val in freq.items() if val>len(nums)//2][0]
        