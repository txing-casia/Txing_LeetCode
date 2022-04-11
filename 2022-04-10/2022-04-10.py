import sys

n,m,k=3,3,4
x,y=[],[]

# squ=[]
# for i in range(n,0,-1):
#     for j in range(m,0,-1):
#         squ.append(i*j)

# squ_s=sorted(squ)
# print(squ_s[-k])

x,d=min(m,n),max(m,n)
flag = 0
for i in range(1,k-1):
    if flag == 1:
        d = d - 1
        x = x + 1
        flag = 0

    if k==1:
        break
    elif d > x and d > 1 and flag == 0:
        # d = d - 1
        s = (d-1)*x
        s_ = d*(x-1)
        if s>=s_:
            d = d - 1
        elif s<s_:
            x = x - 1
    elif x > d and x > 1 and flag == 0:
        s = (d-1)*x
        s_ = d*(x-1)
        if s>=s_:
            d = d - 1
        elif s<s_:
            x = x - 1
    elif x == d :
        s = (x-1)*(d+1)
        s_ = x*(d-1)
        flag = 1
        if s>=s_ and d+1<max(m,n) and x+1<min(m,n):
            d = d + 1
            x = x - 1-1
        else:
            x = x - 1
    


print(x*d)

