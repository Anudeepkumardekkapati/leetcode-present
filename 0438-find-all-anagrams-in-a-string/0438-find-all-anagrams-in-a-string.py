class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        
        len1=len(s)
        len2=len(p)
        p="".join((sorted(p)))
      
        for i in range(len1-(len2-1)):
            lists=sorted(s[i:i+len2])
            if ("".join(lists))==((p)):
                ans.append(i)
        return(ans)
                