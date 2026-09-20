class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        a={'+','-','/','*'}
        stk=[]
        for i in tokens:
            if i not in a:
                stk.append(int(i))
            else:
                c=stk.pop()
                b=stk.pop()
                if i=='+':
                    stk.append(b+c)
                elif i=='-':
                    stk.append(b-c)
                elif i=='*':
                    stk.append(b*c)
                else:
                    stk.append(int(b/c))
        return stk[-1]
    
        