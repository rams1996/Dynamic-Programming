class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if len(s3)==1:
            return s1+s2==s3
        if len(s3)!=(len(s1)+len(s2)):
            return False
        dpMemo=set()
        def recursion(index1,index2,index3):
            if (index1,index2) in dpMemo:
                return False
            if index3==len(s3):
                return True
            if index1<len(s1) and index2<len(s2):
                if s1[index1]==s3[index3] and s2[index2]==s3[index3]:
                    if recursion(index1+1,index2,index3+1):
                        return True
                    if recursion(index1,index2+1,index3+1):
                        return True
                elif s1[index1]==s3[index3]:
                    if recursion(index1+1,index2,index3+1):
                        return True
                elif s2[index2]==s3[index3]:
                    if recursion(index1,index2+1,index3+1):
                        return True
                else:
                    return False
            elif index1<len(s1):
                if s1[index1]==s3[index3]:
                    if recursion(index1+1,index2,index3+1):
                        return True
                else:
                    return False
            elif index2<len(s2):
                if s2[index2]==s3[index3]:
                    if recursion(index1,index2+1,index3+1):
                        return True
                else:
                    return False
            dpMemo.add((index1,index2))
        return recursion(0,0,0)
                
        
