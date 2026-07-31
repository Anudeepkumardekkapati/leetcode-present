class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        maxi=0
        for i in s:
            if i=="(":
                st.append(i)
                length=len(st)
                if length>maxi:
                    maxi=length
            elif i==")":
                st.pop()
        return maxi

        