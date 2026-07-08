class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len=0
        left=0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            max_len = max(right-left+1,max_len)
        return max_len
        