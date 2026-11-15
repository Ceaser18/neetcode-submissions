class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack=[]
        result = [0]*len(arr)
        for i in range(len(arr)):
            while len(stack)>0 and arr[i]>arr[stack[-1]]:
                top=stack.pop()
                result[top]=i-top
            stack.append(i)
        return result
        