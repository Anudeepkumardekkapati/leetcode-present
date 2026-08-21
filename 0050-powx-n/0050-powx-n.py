class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp=n
        if exp<0:
            exp=-exp
            x=1/x
        return self.power(x,exp,1)
    def power(self,x,n,ans):
        if n==0:
            return ans
        if n%2==1:
            ans*=x
        return self.power(x*x,n//2,ans)



        
        