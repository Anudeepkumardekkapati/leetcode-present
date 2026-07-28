class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n

        stack=[]

        for i in range(2*n-1,-1,-1):
            val=i%n
            num=nums[val]
            while stack and stack[-1]<=num:
                stack.pop()
            

            if stack and i<n:
                ans[i]=stack[-1]
            stack.append(num)
        return ans
        