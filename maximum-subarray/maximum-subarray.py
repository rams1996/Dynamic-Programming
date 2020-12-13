class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        total=nums[0]
        newTotal=nums[0]
        for i in range(1,len(nums)):
                newTotal=max(newTotal+nums[i],nums[i])
                if newTotal>total:
                    total=newTotal
                
        return total
            
            
        
