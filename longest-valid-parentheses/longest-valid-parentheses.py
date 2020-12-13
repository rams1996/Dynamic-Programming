class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dic={}
        dic[0]=-1
        level=0
        maxi=0
        for i,j in enumerate(s):
            if j=="(":
                level+=1
                dic[level]=i
            else:
                level-=1
                if level<0:
                    dic={}
                    dic[0]=i
                    level=0
                    continue
                if level in dic:
                    maxi=max(maxi,i-dic[level])
            # print(i,maxi)
        return maxi
                
        
            
            
        
            
        
