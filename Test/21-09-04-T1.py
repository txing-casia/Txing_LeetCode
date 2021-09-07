// 在线面试平台。将链接分享给你的朋友以加入相同的房间。
// Author: tdzl2003<dengyun@meideng.net>

x
def test(x):
    if x < 1:
    	L,H = 0.0,1.0
    else:
        L,H = 1.0,x
    while abs(L - H) <= 0.001:
        M = (L+H) / 2.0
        if M*M < x:
            L = M
        else:
            H = M
    return M

'''
x -> 0, 1
M(x) -> 0, 1

x1, 0
x2, 1
x.....

BatchNorm
'''


f(x) -> [0, 1]

f(x+delta_x)-f(x)

def LocalMinimium(f, init_x):
    alpha = 0.01
    x = init_x
    f1 = f(x)
    f2 = f1+1
    df=[]
    while sum(f1-f2) < 0.1:
       	for i in range(len(x)):
	    	df.append(f(x[i]+alpha) - f(x[i]))
        x_hat = x - alpha * df
        f2 = f(x_hat)
        f1 = f(x)
        x = x_hat
        
    return x
    
    
    
    
    
    
    
    