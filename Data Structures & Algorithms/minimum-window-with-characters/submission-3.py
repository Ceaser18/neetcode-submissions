from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:return ''
        need=Counter(t);l=0;best=float('inf');start=0;window=dict()
        have, required = 0, len(need)
        for r in range(len(s)):
            c = s[r]
            window[c]=window.get(c,0)+1
            if c in need and window[c] == need[c]:
                have += 1
            while have == required:
                if r-l+1<best:
                    best=r-l+1
                    start=l
                window[s[l]]-=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                if window[s[l]]==0:
                    del window[s[l]]
                l+=1
        return '' if best==float('inf') else s[start:start+best]