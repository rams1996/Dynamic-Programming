class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def dfs(total,c):
            if total in dp:
                return dp[total]
            if total==n:
                return 1
            if total>n:
                return 0
            a=dfs(total+1,c+1)
            b=dfs(total+2,c+1)
            dp[total]=a+b
            return a+b
        return dfs(0,0)
