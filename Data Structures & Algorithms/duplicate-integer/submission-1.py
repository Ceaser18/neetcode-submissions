class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        seen={}
        for num in arr:
            if num in seen:
                return True 
            seen[num]=True
        return False