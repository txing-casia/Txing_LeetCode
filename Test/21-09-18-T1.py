# 二叉树转化为链表
class TreeNode():
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


    def tree2list(self,root):
        if not root:
            return None
        queue = []
        queue.append(root)
        while len(queue)>0:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            elif node.right:
                queue.append(node.right)
            elif node.left == None:
                queue.append('*')
            elif node.right == None:
                queue.append('*')
        return str(queue)


def main():
    A = TreeNode('A','B','C')
    B = TreeNode('B',None,'D')
    C = TreeNode('C','E','F')
    E = TreeNode('E','G',None)
    F = TreeNode('F',None,'I')
    sol = TreeNode().tree2list(A) 
    print(sol)

if __name__ == '__main__':
    main()

