class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        return len(arr)!=len(set(arr))