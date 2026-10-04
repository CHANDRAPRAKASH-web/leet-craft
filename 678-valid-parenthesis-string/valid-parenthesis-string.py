class Solution:
    def checkValidString(self, s: str) -> bool:
        d=0
        for i in s:
            if i=='*' or i=='(':
                d+=1
            else:
                d-=1
            if d<0:
                return False
        
        d=0
        for i in s[::-1]:
            if i=='*' or i==')':
                d+=1
            else:
                d-=1
            if d<0:
                return False
        return True
        