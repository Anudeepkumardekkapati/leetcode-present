class Solution:
    def calculate(self, s: str) -> int:
       

        ops=[]
        nums=[]
        num=0

        for i in range(len(s)):
            if s[i]==" ":
                continue
            elif s[i].isdigit():
                num=num*10+int(s[i])

            else:
                nums.append(num)
                ops.append(s[i])
                num=0
        nums.append(num)


        i=0
        while i<(len(ops)):
            if ops[i]=='*' or ops[i]=='/':
                if ops[i]=='*':
                    first=nums[i]
                    second=nums[i+1]
                    val=first*second
                else:
                    first=nums[i]
                    second=nums[i+1]
                    val=first//second

                nums[i]=val
                nums.pop(i+1)
                ops.pop(i)

            else:
                i+=1


        result=nums[0]
        i=0
        while i<len(ops):
            if ops[i]=='+':
                result+=nums[i+1]
            else:
                result-=nums[i+1]
            i+=1
        return result
                