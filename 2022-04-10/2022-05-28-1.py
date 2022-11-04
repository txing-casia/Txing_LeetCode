    
try:
    HP = 1
    nums = list(map(int,input().strip().split()))
    sortnums=sorted(nums)
    step=0
    for a in sortnums:
        while a>0:
            a=a-HP
            step+=1
        HP+=1
    print(step)
except:
    pass