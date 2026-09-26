class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        a={}
        for i in knowledge:
            a[i[0]]=i[1]
        start=False
        curr=""
        res=[]
        for i in s:
            if i=='(':
                start=True
            elif i==')':
                v=a.get(curr,'?') 
                res.append(v)
                curr=''
                start=False
            elif start==False:
                res.append(i)
            elif start==True:
                curr+=i
        return "".join(res)