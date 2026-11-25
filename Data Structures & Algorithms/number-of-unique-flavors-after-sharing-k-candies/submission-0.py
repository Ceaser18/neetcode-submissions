from collections import Counter
class Solution:
    def shareCandies(self, arr: List[int], k: int) -> int:
        l=0;best=0
        kept=Counter(arr) # this returns a dict
        for r in range(len(arr)):
            # I'd have to give away this candy 
            kept[arr[r]]-=1
            if kept[arr[r]]==0:
                del kept[arr[r]]
            while r-l+1>k:
                # now ill take back from her
                kept[arr[l]]=kept.get(arr[l],0)+1
                l+=1
            if r-l+1 ==k:
                best=max(best,len(kept))
        return best

