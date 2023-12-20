import math
print("         TABLE OF TRIGONOMETRIC FUNCTIONS")
print("         ================================")
print("N\t   Sin\t\t  Cos\t\t   Tan")
for i in range(0, 50, 5):
    d = math.radians(i)
    s = math.sin(d)
    c = math.cos(d)
    t = math.tan(d)
    print(i, "\t%9.7f\t%9.7f\t%9.7f" %(s,d,t))
