class Solution:
    def distinctNumbers(self, arr: List[int], k: int) -> List[int]:
        l=0;result=[];freq=dict()
        for r in range(len(arr)):
            freq[arr[r]]=freq.get(arr[r],0)+1
            while r-l+1>k:
                freq[arr[l]]-=1
                if freq[arr[l]]==0:
                    del freq[arr[l]]
                l+=1
            if r-l+1 == k:
                result.append(len(freq))
        return result