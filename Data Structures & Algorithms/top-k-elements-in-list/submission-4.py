from collections import Counter
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        freq = Counter(arr)
        buckets = [[] for _ in range(len(arr)+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        result=[]
        for i in range(len(buckets)-1,0,-1): # this loop goes backwars with the pointer i
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result
        return result