class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        directions=((1,0),(0,1))
        dpMemo={}
        def dfs(i,j):
            if ((i,j)) in dpMemo:
                return dpMemo[(i,j)]
            if i<0 or i>=len(obstacleGrid) or j<0 or j>=len(obstacleGrid[0]):
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
                return 1
            count=0
            for dirs in directions:
                r=i+dirs[0]
                c=j+dirs[1]
                count+=dfs(r,c)
            dpMemo[(i,j)]=count
            return count
            
            
            
            
            
            
            
            
        return dfs(0,0)
        
