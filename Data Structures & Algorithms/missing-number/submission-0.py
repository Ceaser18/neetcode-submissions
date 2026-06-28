class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n=len(arr)
        expected = n*(n+1)//2
        return expected - sum(arr)
        