class Solution:
    def isValid(self, s: str) -> bool:
        map={')':'(',']':'[','}':'{'}
        stk=[]
        for i in s:
            if i not in map:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    a=stk.pop()
                    if a!=map[i]:
                        return False
        return not stk