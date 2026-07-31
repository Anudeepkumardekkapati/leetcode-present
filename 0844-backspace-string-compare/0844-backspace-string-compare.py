class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first=[]
        second=[]
        for i in s:
            if i=="#":
                if first:

                    first.pop()
            else:
                first.append(i)
        

        for j in t:
            if j=="#":
                if second:
                    second.pop()
            else:
                second.append(j)
        
        if first==second:
            return True
        else:
            return False
        