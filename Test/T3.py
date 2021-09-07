links=str([[1,2,5],[1,3,5],[4,2,10],[2,5,5],[3,4,10],[3,7,10],[4,7,5],[5,6,5],[6,7,5]])
# links=links.strip(']').strip('[').replace(']','').replace('[','').replace(',',' ')
links=links.replace(']','').replace('[','').replace(',',' ')

print(links)

links = list(map(int,links.split()))



N=len(links)//3
   
old_ans = 0
flag = -1
for i in range(N-1):
    new_ans = abs(links[i*3+0]-links[i*3+1])
    if new_ans > old_ans:
        old_ans = new_ans
        flag = links[i*3+2]
print(old_ans*flag)