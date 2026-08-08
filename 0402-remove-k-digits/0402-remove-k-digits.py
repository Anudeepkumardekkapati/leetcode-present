class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack=[]
        for i in nums:
            while stack and k>0 and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
            

        while stack and k>0:
            stack.pop()
            k-=1

        res="".join(stack).lstrip('0')
        if res:
            return res
        else:
            return "0"
        