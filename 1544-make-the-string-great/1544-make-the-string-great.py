class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            val=i

            if (stack and stack[-1].isupper() and val.islower() and (stack[-1].lower())==val.lower()) or (stack and stack[-1].islower() and val.isupper() and (stack[-1].lower())==val.lower()):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

        