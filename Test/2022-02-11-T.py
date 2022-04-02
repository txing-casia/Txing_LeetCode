

def calweight( stones) -> int:
    while len(stones)>=2:
        i = stones.index(max(stones))
        x = stones[i]
        stones.pop(i)

        j = stones.index(max(stones))
        y = stones[j]
        stones.pop(j)

        if x == y:
            rest = 0
        else:
            rest = abs(x-y)
            stones.append(rest)
    if stones:
        print(stones[0])
    else:
        print(0)



a=[2,7,4,1,8,1]

calweight(a)

