class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        l=0
        res=""
        def expand(low,high):
            
            while low>=0 and high<len(s) and s[low]==s[high]:
                low-=1
                high+=1
                
            return s[low+1:high]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                val=expand(i-2,i+1)
                if len(val)>l:
                    res=val
                    l=len(val)
            val=expand(i-1,i+1)
            if len(val)>l:
                res=val
                l=len(val)
        return res
            
        
        
        
                    
                
