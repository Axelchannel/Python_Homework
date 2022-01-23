#Найти расстояние между точками в пространстве 2D/3D
#формула поиска расстояния между токами A и B = корень(xB - xA)^2 + (yB - yA)^2 + (zB - zA)^2;

import math


def DistanationPoint2D(x1,x2,y1,y2):
    return math.sqrt((math.pow((x2-x1),2)+math.pow((y2-y1),2)))

def DistanationPoint3D(x1,x2,y1,y2,z1,z2):
    return math.sqrt((math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2)))

print(DistanationPoint2D(2, 3, -5, -7))