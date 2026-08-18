class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for i in range(m):
            row=[0]*n
            dp.append(row)


        return self.paths(m-1,n-1,dp)
    def paths(self,row,col,dp):
        if row==0 or col==0:
            return 1
        if dp[row][col]!=0:
            return dp[row][col]
        else:
            dp[row][col]=self.paths(row-1,col,dp)+self.paths(row,col-1,dp)
            return dp[row][col]
        
  

        