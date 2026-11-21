class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        freq={};best=0;l=0
        for r in range(len(arr)):
            freq[arr[r]]=freq.get(arr[r],0)+1
            while len(freq)>2:
                freq[arr[l]]-=1
                if freq[arr[l]]==0:
                    del freq[arr[l]]
                l+=1
            best=max(best,r-l+1)
        return best
        