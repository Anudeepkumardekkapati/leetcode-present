class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        nums=[]

        for i in tokens:
            if i in "+/*-":
                if nums:
                    second=nums.pop()
                    first=nums.pop()
                    

                    if i=='+':
                        
                        val=first+second
                    

                    elif i=='-':
                        
                        val=first-second
                    
                    elif i=='*':
                    
                        val=first*second
                    
                    elif i=='/':
                        
                        val=int(first/second)
                    elif i=='^':
                                    
                        val=first**second
                    nums.append(val)
                        
            else:

                nums.append(int(i))
        return(nums[0])

                