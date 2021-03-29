import math
from enum import Enum
import bisect
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

def stringToListNode(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]" # 最后一个逗号不输出




class Solution:
    def copyRandomList(self, head) :
        def dfs(head):
            if not head: return None # 判断遍历链表结束
            if head in visited: # 结点已存在，返回结点避免重复复制
                return visited[head]
           
            copy = Node(head.val, None, None) # 创建新结点
            visited[head] = copy # hash中增加一个结点
            copy.next = dfs(head.next) 
            copy.random = dfs(head.random)
            return copy

        visited = {} # 创建存放结点的链表
        return dfs(head) # 最后返回头指针

class Solution:
    def copyRandomList1(self, head: 'Node') -> 'Node':
        visited = {}
    
        def bfs(head):
            if not head: return head # 判断遍历链表结束
            clone = Node(head.val, None, None) # 创建新结点
            queue = collections.deque() # 双端数列
            queue.append(head)
            visited[head] = clone # 结点存入hash
            while queue:
                tmp = queue.pop() # 
                if tmp.next and tmp.next not in visited: # .next结点非空且未复制
                    visited[tmp.next] = Node(tmp.next.val, [], [])
                    queue.append(tmp.next)  
                if tmp.random and tmp.random not in visited: # .random结点非空且未复制
                    visited[tmp.random] = Node(tmp.random.val, [], [])
                    queue.append(tmp.random)
                visited[tmp].next = visited.get(tmp.next) # 字典get()函数返回指定键的值
                visited[tmp].random = visited.get(tmp.random)
            return clone # 返回头指针
        return bfs(head)

class Solution:
    def copyRandomList2(self, head: 'Node') -> 'Node':
        visited = {}
        def getClonedNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val,None,None)
                    return visited[node]
            return None
        
        if not head: return head
        old_node = head
        new_node = Node(old_node.val,None,None)
        visited[old_node] = new_node

        while old_node:
            new_node.random = getClonedNode(old_node.random)
            new_node.next = getClonedNode(old_node.next)
            
            old_node = old_node.next
            new_node = new_node.next
        return visited[head]









def main():
    head = stringToListNode([[7,None],[13,0],[11,4],[10,2],[1,0]])
    solution=Solution().copyRandomList(head)
    print(solution)


if __name__ == "__main__":
    main()


