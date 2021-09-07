给定一棵n个点的有根树，第i个点的父节点是fa[i]，每个点权值为A[i].

称点i和点j是兄弟 (i != j)，当且仅当fa[i]=fa[j].

求出一个点集，这个点集里至多只有一对兄弟，使得权值和最大。

n <= 1,000,000, -100000 <= A[i] <= 1000000


class Node:
   Node fa
   int value

    fa == None

def findMax(nodes: list[Node]):
    hash={}
    node_list=[[None]*len(nodes) for _ in range(len(nodes))]
    j = 0 # 父节点序号
    for i in range(len(nodes)):
    	if nodes[i].fa in hash:
            node_list[hash[nodes[i].fa]].append(nodes[i]) 
        else:
            hash[nodes[i].fa] = j
    		node_list[hash[nodes[i].fa]].append(nodes[i])
            j += 1
    
	n = len(nodes)
    ans = -100000
    for p in range(j):
        for q in range(len(node_list[p])):
        	val_list.append(node_list[p][q].value)
        
        res = sum(sorted(val_list)[0:2])
	    ans = max(ans,res)
    
    return ans
    
    
    {X Y Z A B}
    A > B
    A < 0
    {X Y Z} 
    
    
'''
    def DFS(num, nodes):# 遍历到第num个结点，并以这个结点为父节点
        if num == len(nodes) or nodes(num+1).fa != nodes(num):
            return -100000
        son = []
	    for i in range(num+1,len(nodes)):
        	if nodes[i+1].fa == nodes[i].fa:
    			son.append(nodes[i])
            else:
                break
        res = sorted(son)[0:2]
        
        return  max(res,DFS(num+1,nodes))
	'''
        
        
        
        
        
        
        
                