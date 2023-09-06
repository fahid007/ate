
from math import sqrt
x1= int(input("x1 coordinate:"))
y1= int(input("y1 coordinate:"))
x2= int(input("x2 coordinate:"))
y2= int(input("y2 coordinate:"))
x=tuple([x1, y1])
y=tuple([x2, y2])
dist= sqrt(((x2-x1)**2)+((y2-y1)**2))
print("distance=", dist)