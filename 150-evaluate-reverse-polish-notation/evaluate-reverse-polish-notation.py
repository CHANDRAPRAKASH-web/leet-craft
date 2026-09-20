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
                    stk.append(int(b)+int(c))
                elif i=='-':
                    stk.append(int(b)-int(c))
                elif i=='*':
                    stk.append(int(b)*int(c))
                else:
                    b=int(b)
                    c=int(c)
                    stk.append(int(b/c))
        return stk[-1]
    
        