class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        d=0
        res=0
        for i in s:
            if i=='(':
                d+=1
            if i==')':
                d-=1
            if d<0:
                d+=1
                res+=1
        return res+d
        