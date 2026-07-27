class Solution:
    def searchMatrix(self, nums: List[List[int]], t: int) -> bool:
        rows=len(nums)
        cols=len(nums[0])



        l=0
        r=rows*cols-1
        while(l<=r):
            mid=(l+r)//2

            row=mid//cols
            col=mid%cols

            if nums[row][col]==t:
                return True
            elif nums[row][col]>t:
                r=mid-1
            else:
                l=mid+1
        return False