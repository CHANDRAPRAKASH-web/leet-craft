class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d=0
        res=0
        prev=''
        for i in s:
            if i=='(':
                d+=1
            else:
                d-=1
            if i==')' and prev=='(':
                res+=1<<d
            prev=i
        return res
        