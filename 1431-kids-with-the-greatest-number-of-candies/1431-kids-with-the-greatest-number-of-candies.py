class Solution:
    def kidsWithCandies(self, nums: List[int], extra: int) -> List[bool]:
        ans=[]


        for i in range(len(nums)):
            if nums[i]+extra >= max(nums):
                ans.append(True)
            else:
                ans.append(False)
        return ans
