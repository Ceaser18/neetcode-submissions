class Solution:
    def maxDifference(self, s: str) -> int:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0) +1
        even = [val for num,val in freq.items() if val%2==0]
        odd = [val for num,val in freq.items() if val%2!=0]
        return max(odd)-min(even)