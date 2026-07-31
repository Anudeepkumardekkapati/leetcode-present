class Solution:
    def largestRectangleArea(self,nums: List[int]) -> int:
        maxi=0
        st=[]

        n=len(nums)
        for i in range(n+1):
            if i==n:
                h=0
            else:
                h=nums[i]

            while st and h<nums[st[-1]]:
                height=nums[st.pop()]
                if not st:
                    width=i
                else:
                    width=i- st[-1]-1

                area=height*width

                maxi=max(maxi,area)
            st.append(i)
        return maxi     
        