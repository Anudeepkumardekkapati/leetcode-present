class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map={}
        for i in reversed(nums2):
            while stack and stack[-1]<=i:
                stack.pop()
            

            if stack:
                map[i]=stack[-1]
            else:
                map[i]=-1
            stack.append(i)
        
        ans=[]
        for i in nums1:
            ans.append(map[i])
        return ans
            