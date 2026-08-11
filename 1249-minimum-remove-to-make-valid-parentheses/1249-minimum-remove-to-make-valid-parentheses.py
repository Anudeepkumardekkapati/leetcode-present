class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        sets=set()

        for i in range (len(s)):
            if s[i]=='(':
                stack.append(i)
            
            elif s[i]==')':
                if stack:
                    stack.pop()
                else:
                    sets.add(i)
        
        for i in stack:
            sets.add(i)
        


        ans=""
        for i in range (len(s)):
            if i not in sets:
                ans+=s[i]
        return ans