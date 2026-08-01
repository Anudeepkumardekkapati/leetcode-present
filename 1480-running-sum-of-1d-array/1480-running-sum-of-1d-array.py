class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        sums=0
        for i in nums:
            sums+=i
            ans.append(sums)
        return ans


        