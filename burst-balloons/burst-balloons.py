class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dpMemo = {}
        
​
        def recursion(left, right):
            if (left, right) in dpMemo:
                return dpMemo[(left, right)]
            maximum = 0
            for i in range(left + 1, right):
                a=recursion(left,i)
                b=recursion(i,right)
                maximum = max(maximum, a +b + nums[left] * nums[i] * nums[right])
            dpMemo[(left, right)] = maximum
            return maximum
        return recursion(0, len(nums) - 1)
                
     
    
    
                    
                    
        
        
        
        
