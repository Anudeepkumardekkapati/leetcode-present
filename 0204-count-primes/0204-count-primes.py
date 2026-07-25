class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0 
     
        emt=[True]*n

        emt[0]=False
        emt[1]=False

        for i in range(2,n):
          
                for j in range(i*i,n,i):
                    emt[j]=False

        return sum(emt)
            
        