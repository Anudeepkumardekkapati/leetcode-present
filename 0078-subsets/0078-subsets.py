class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in nums:
            temp=[]
            for j in ans:
                temp.append(j+[i])
            ans+=(temp)
        return ans
                
                