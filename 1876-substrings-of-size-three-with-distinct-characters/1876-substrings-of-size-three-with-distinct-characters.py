class Solution:
    def countGoodSubstrings(self, s: str) -> int:


     

        count=0
        temp=[]
        for i in range(len(s)):
            
            if len(temp)>=3:
                temp.pop(0)
            
            temp.append(s[i])
            if len(temp)==3:
                map={}
                for j in temp:
                    if j not in map:
                        map[j]=1
                    else:
                        map[j]+=1
                    if len(map)==3:
                        count+=1 
        return(count)


        