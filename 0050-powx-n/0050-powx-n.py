class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n<0:
            x=1/x
            n=-n
        return self.pow(x,n,1)
    def pow(self,x,n,ans):
        if n==0:
            return ans
        if n%2!=0:
            ans*=x
     
        return self.pow(x*x,n//2,ans)

                

        
        