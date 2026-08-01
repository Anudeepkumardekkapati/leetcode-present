class Solution:
    def restoreString(self, s: str, list: List[int]) -> str:
        map={}
        for i in range(len(s)):
            map[list[i]]=s[i]

        res=""
        for i in range(len(map)):
            res+=map[i] 
        return res      