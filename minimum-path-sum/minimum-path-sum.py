class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions=((1,0),(0,1))
        minimum=float('inf')
        dpMemo={}
        def helper(i,j,total):
            #Base
            if (i,j) in dpMemo:
                return dpMemo[(i,j)]+total
            if i>=len(grid) or j>=len(grid[0]):
                return float('inf')
            if i==(len(grid)-1) and j==(len(grid[0])-1):
                total+=grid[i][j]
                return total
    
            #Logic
            sum=float('inf')
            for dirs in directions:
                sum=min(helper(i+dirs[0],j+dirs[1],total+grid[i][j]),sum)
            dpMemo[(i,j)]=sum-total
            return sum
        return helper(0,0,0)
        
