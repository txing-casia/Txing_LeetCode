def test(x):
    if x < 1:
    	L,H = 0.0,1.0
    else:
        L,H = 1.0,x
    while abs(L - H) >= 0.001:
        M = (L+H) / 2.0
        if M*M < x:
            L = M
        else:
            H = M
    return M

print(test(10))