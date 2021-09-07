# 100%

import math
import sys

try:
    N =input().split()
    for num in range(int(N[0])):
        x,y,r = map(float,input().strip().split(' '))
        temp = 0
        if r == abs(x):
            temp+=1
        elif  r > abs(x):
            temp+=2
        if r == abs(y):
            temp+=1
        elif  r > abs(y):
            temp+=2
        if pow(pow(abs(x),2)+pow(abs(y),2),0.5) == r:
            temp-=1
        print(temp)
        
except:
    pass