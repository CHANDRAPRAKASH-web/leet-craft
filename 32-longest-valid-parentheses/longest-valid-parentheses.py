class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        def calc(s,o,c):
            d=0
            res=0
            l=0
            for r in range(n):
                if s[r]=='(':
                    d+=o
                else:
                    d+=c
                if d<0:
                    d=0
                    l=r+1
                if d==0:
                    res=max(res,r-l+1)
            return res
        return max(calc(s,1,-1),calc(s[::-1],-1,1))
        
        