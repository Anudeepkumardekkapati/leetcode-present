class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            
            else:
                substring=""
                while stack[-1]!='[':
                    substring=stack.pop()+substring
                
                stack.pop()

            
                nums=""
                while stack and stack[-1].isdigit():
                    nums=stack.pop()+nums

                rep=int(nums)

                stack.append(rep*substring)
        return "".join(stack)

        