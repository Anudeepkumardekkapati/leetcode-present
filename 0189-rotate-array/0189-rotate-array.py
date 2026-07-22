class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        n=len(nums)
        temp=[0]*n
        k=k%n
        for i in range(n):
            some=(i+k)%n
            temp[some]=nums[i]

        for i in range(n):
            nums[i]=temp[i]

                