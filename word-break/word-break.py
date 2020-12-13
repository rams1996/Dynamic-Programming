class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dpMemo={}
        wordDict=set(wordDict)
        def helper(index):
            #Base
            if index in dpMemo:
                return dpMemo[index]
            if index==len(s):
                return True
            #Logic
            for i in range(index+1,len(s)+1):
                if s[index:i] in wordDict:
                    if helper(i):
                        return True
            dpMemo[index]=False
            return False
        return helper(0)
                
                
                
                
                
    
    
                
            
            
        
