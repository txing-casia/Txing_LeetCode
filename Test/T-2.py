# 75%
import math
import sys

a,b,c=1.0,1.0,2.0

x1_1=(-b)/(2*a)
x1_2=pow(pow(b,2)-4*a*c,0.5)/(2*a)
x2_1=(-b)/(2*a)
x2_2=-pow(pow(b,2)-4*a*c,0.5)/(2*a)
if pow(b,2)-4*a*c>=0:
    print(int(x1_1+x1_2))
    print(int(x2_1+x2_2))
else:
    print(str(int(x1_1+x1_2.real))+' '+str(x1_2.imag))
    print(str(int(x2_1+x2_2.real))+' '+str(x2_2.imag))



