class Solution:
    def calPoints(self, nums: List[str]) -> int:
        st=[]
        for i in range(len(nums)):
            if nums[i]=="C":
                st.pop()
            elif  nums[i]=="D":
                val=int(st[-1])*2
                st.append(val)
            elif   nums[i]=="+":
                vals=int(st[-1])+int(st[-2])
                st.append(vals)

            else:
                st.append(int(nums[i]))
        return(sum(st))

        