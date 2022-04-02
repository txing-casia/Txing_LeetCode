

def search(L,a):
    N = len(L)
    left = 0
    right = N - 1 
    mid = (left + right) // 2
    while left <= right:
        if L(mid) < a:
            left = mid 
        elif L(mid) > a:
            right = mid
        elif L(mid) == a:
            return L(mid)
    return None




L = [1,2,3,4,5,6,7,8,9,10]
a = 3 
print(search(L,a))