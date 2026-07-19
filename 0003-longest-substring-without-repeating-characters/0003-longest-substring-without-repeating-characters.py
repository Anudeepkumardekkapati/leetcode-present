class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxi=0
        sets=set()
        left=0
        if set(s)==1:
            
            return len(s)-1
        for i in range(len(s)):
            if s[i] not in sets:
                sets.add(s[i])
            

            else:
                while(s[i] in sets):
                    sets.remove(s[left])
                    left+=1
                sets.add(s[i])
            maxi=max(maxi,len(sets))
        return maxi
                
        