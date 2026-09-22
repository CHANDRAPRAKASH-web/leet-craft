class Solution:
    def simplifyPath(self, path: str) -> str:
        components=path.split('/')
        stack=[]
        for i in components:
            if i=="..":
                if stack:
                    stack.pop()
            elif i not in ["","."]:
                stack.append(i)
    
        return "/"+"/".join(stack)

        