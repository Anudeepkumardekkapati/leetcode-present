class Solution:
    def calPoints(self, nums: List[str]) -> int:

        st=[]
        for i in nums:
            if st and i=="+":
                first=int(st[-1])
                second=int(st[-2])
                st.append(first+second)
            
            elif st and i=="D":
                prev=int(st[-1])*2
                st.append(prev)
            elif st and i=="C":
                st.pop()
            else:
                st.append(int(i))
        return sum(st)

        