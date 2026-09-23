class Solution:
    def calculate(self, s: str) -> int:
        i=0
        cur_operation='+'
        res=0
        cur=0
        prev=0
        while i<len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                        cur=cur*10+int(s[i])
                        i+=1
                i-=1
                if cur_operation=='+':
                    res+=cur
                    prev=cur
                elif cur_operation=='-':
                    res-=cur
                    prev=-cur
                elif cur_operation=='*':
                    res-=prev
                    res+=(prev*cur)
                    prev=prev*cur
                elif cur_operation=='/':
                    res-=prev
                    res+=int(prev/cur)
                    prev=int(prev/cur)
            elif s[i]!=" ":
                cur_operation=s[i]
                
            cur=0
            i+=1
        return res


        