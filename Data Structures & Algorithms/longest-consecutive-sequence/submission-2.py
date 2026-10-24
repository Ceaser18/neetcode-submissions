class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        nums = set(arr)
        longest=0
        for num in nums:
            if num-1 not in nums:
                current=num
                while current+1 in nums:
                    current+=1
                longest = max(longest,current-num+1)
        return longest