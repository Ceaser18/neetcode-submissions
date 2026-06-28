class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        for ch in s:
            seen[ch]=seen.get(ch,0)+1
        for ch in t:
            seen[ch]=seen.get(ch,0)-1 
        return all(val==0 for val in seen.values())
        