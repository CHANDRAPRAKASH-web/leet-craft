class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1>xCenter:
            closestx=x1
        elif x2<xCenter:
            closestx=x2
        else:
            closestx=xCenter

        if y1>yCenter:
            closesty=y1
        elif y2<yCenter:
            closesty=y2
        else:
            closesty=yCenter

        distance=(((closestx-xCenter)**2)+((closesty-yCenter)**2))**(0.5)
        return distance<=radius