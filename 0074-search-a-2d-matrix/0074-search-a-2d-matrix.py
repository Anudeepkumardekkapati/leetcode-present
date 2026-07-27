class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        rows=len(nums)
        cols=len(nums[0])

        for i in range(rows):
            for j in range(cols):
                if(nums[i][j])==target:
                    return(True)
        return False
        