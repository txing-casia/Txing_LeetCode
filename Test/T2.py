class linklist:
    def __init__(self,x):
        self.next = None
        self.val = x
        
def string2linklist(input):
    dummyroot = linklist(0)
    ptr = dummyroot 
    for num in input:
        ptr.next = linklist(num)
        ptr = ptr.next
    ptr = dummyroot
    return ptr
    
num = string2linklist([1,2,3,2,1])
print(num)
# print(string2linklist(num))