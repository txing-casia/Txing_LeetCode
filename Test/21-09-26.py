class TreeNode:
    def treenode(self,data=None,left=None,right=None):
        self.date=data
        self.right=right
        self.left=left


def create(L):
    if not L :
        return None
    n = len(L)
    if n == 1:
        newNode = TreeNode(L(n // 2), None, None)
    elif n == 2:
        newNode = TreeNode(L(n // 2), L(n//2-1), None)
    elif n == 3:
        newNode = TreeNode(L(n // 2), L(n//2-1), L(n//2+1))
    return newNode

List = [2,3,1,4,5]

def sort_list(L):
    M = len(L)
    for i in range(M):
        for j in range(i,M):
            if L[i]>L[j]:
                L[i],L[j] = L[j],L[i]
                




# N = len(List)
# L = List 
# while :
#     L = 
#     create(L)

root = TreeNode(List(N // 2), List(N//2-1), List(N//2+1))


