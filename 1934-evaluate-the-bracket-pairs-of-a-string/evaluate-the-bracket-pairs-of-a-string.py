class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        a={}
        for i in knowledge:
            a[i[0]]=i[1]
        started=False
        curr=""
        res=""
        for i in s:
            if i=='(':
                started=True
            elif i==')':
                v=a.get(curr,'?') 
                res+=v
                curr=''
                started=False
            elif started==False:
                res+=i
            elif started==True:
                curr+=i
        return res       