class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:


        stack=[]
        rem=len(nums)-k
        for i in nums:




            while stack and stack[-1]>i and rem>0:
                stack.pop()
                rem-=1
            stack.append(i)


        return stack[:k]
        