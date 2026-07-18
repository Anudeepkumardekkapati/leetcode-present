class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        
        len1=len(s)
        len2=len(p)
        map_s=[0]*26
        map_p=[0]*26

        for i in p:
            map_p[ord(i)-ord('a')]+=1
        
        for j in s[:len2]:
            map_s[ord(j)-ord('a')]+=1
        

        if map_s==map_p:
            ans.append(0)
        

        for k in range(len2,len1):
            old=s[k-len2]
            map_s[ord(old)-ord('a')]-=1

            new=s[k]
            map_s[ord(new)-ord('a')]+=1
            if map_s==map_p:
                ans.append(k-len2+1)
        return ans