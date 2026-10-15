class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        first=sum(nums[:k])
        maxi=(first)
        for i in range(k,len(nums)):
            first+=nums[i]-nums[i-k]
            maxi=max(maxi,first)
        return maxi/k

        