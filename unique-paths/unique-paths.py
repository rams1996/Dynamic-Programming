class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions=((1,0),(0,1))
        
        dpMemo={}
        def dfs(i,j):
            if (i,j) in dpMemo:
                return dpMemo[(i,j)]
            if i<0 or i>m or j<0 or j>n:
                return 0
            if i==m and j==n:
                return 1
            count=0
            for dirs in directions:
                r=i+dirs[0]
                c=j+dirs[1]
                count+=dfs(r,c)
            dpMemo[(i,j)]=count
            return count
        return dfs(1,1)
        
