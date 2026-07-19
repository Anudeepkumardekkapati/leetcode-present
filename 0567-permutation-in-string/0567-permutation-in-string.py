class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        freq1=[0]*26
        freq2=[0]*26
        ans=False
        left=0
        for i in s1:
            freq1[ord(i)-ord('a')]+=1
        


        for right in range(l2):
            freq2[ord(s2[right])-ord('a')]+=1
        
            if right-left+1 >l1:
                freq2[ord(s2[left])-ord('a')]-=1
                left+=1
            if right-left+1==l1:
                if freq1==freq2:
                    ans=True
        return ans

        


        
        
        