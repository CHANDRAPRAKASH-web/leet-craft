class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        max_area=0
        stack=[]
        for i,val in enumerate(heights):
            if stack and val<stack[-1][0]:
                while stack and val<stack[-1][0]:
                    a=stack.pop()
                    h=a[0]
                    w=i-a[1]
                    max_area=max(max_area,h*w)
                stack.append((val,a[1]))
            if not stack or val>stack[-1][0]:
                stack.append((val,i))

        for i in stack:
            h=i[0]
            w=n-i[1]
            max_area=max(max_area,h*w)

        return max_area
               
            