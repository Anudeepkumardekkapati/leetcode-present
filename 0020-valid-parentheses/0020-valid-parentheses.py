class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        if s[0]==')' or s[0]=='}' or s[0]==']':
            return False
        st=[]
        for i in s:
            if i=='(':
                st.append(i)
            elif i=='[':
                st.append(i)
            elif i=='{':
                st.append(i)
            elif i==')':

                if i==')' and st and st[-1]=='(':
                    st.pop()
                else:
                    return False
            elif i==']':

                if i==']' and st and st[-1]=='[':
                    st.pop()
                else:
                    return False
            elif i=='}':
                if i=="}" and st and st[-1]=='{':
                    st.pop()
                else:
                    return False
        return len(st)==0

                