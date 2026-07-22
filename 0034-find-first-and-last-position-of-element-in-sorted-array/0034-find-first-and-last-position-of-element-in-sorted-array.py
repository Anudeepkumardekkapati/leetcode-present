class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        if t not in nums:
            return [-1,-1]

        def first(nums,t):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==t:
                    r=mid-1
                elif nums[mid]>t:
                    r=mid-1
                else:
                    l=mid+1
            return l

        

        def last(nums,t):
            
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==t:
                    l=mid+1
                elif nums[mid]>t:
                    r=mid-1
                else:
                    l=mid+1
            return r
        first= first(nums,t)
        last=last(nums,t)

        return [first,last]


            



        